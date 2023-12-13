from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from branca.element import JavascriptLink

from .models import *
from main.models import UserProfile

import folium, clipboard

alltimes = ['10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00', '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00', '14:00-14:30', '14:30-15:00', '15:00-15:30', '15:30-16:00', '16:00-16:30', '16:30-17:00', '17:00-17:30', '17:30-18:00', '18:00-18:30', '18:30-19:00', '19:00-19:30', '19:30-20:00', '20:00-20:30', '20:30-21:00', '21:00-21:30', '21:30-22:00']

start_location = [50.0755, 14.4378]

def manageSpots(request):
    if not request.user.is_staff:
        messages.error(request, "K přístupu na tuto stránku nemáte dostatečná oprávnění")
        return redirect('home')

    if request.method == 'POST':
        c = request.POST.get('coordinates')
        name = request.POST.get('name')
        desc = request.POST.get('description')
        times = []
        for t in alltimes:
            if request.POST.get(t) is not None: times.append(t)

        try: lan, lon = c.split(',')
        except: request.messages('error', 'Wrong coordinates')

        slots = ""

        for t in times: slots += str(t) + ';'
        if int(request.POST.get('spot_id')) == -1:
            s = Spot.objects.create(
                lan = lan,
                lon = lon,
                name = name,
                description = desc,
                allowedSlots = slots
            )
        else:
            try:
                s = Spot.objects.get(id = request.POST.get('spot_id'))
                s.lan = lan
                s.lon = lon
                s.name = name
                s.description = desc
                s.allowedSlots = slots
                s.save()
            except Exception as e: print("Couldn't edit the requested spot: " + str(e))
        
    m = folium.Map(location=(start_location[0], start_location[1]), zoom_start=13)

    for s in Spot.objects.all():
        print('adding '+ s.name +' at: ' + str(s.lan)+'; '+  str(s.lon))
        folium.Marker(
            location=[+s.lan, +s.lon],
            tooltip="Zobrazit informace",
            popup=f"""<b>{s.name}</b><br>
            <button class='edit-spot btn btn-outline-primary' id='edit{s.id}' onclick='editSpot(this)'>Upravit</button>
            <button class='del-spot btn btn-outline-danger' id='delete{s.id}' onclick='deleteSpot(this)'>Smazat lokaci</button>
            """,
            icon=folium.Icon(color="blue", icon="music")
        ).add_to(m)

    m.add_child(folium.ClickForMarker(popup="<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}<br>"))
    m.add_child(folium.ClickForLatLng(alert=False))

    

    m.get_root().html.add_child(JavascriptLink('../static/js/spot_manage_iframe.js'))

    times = open('static/times.txt', 'r').read()
    times = times.split('\n')
    t_arr = []
    for t in times:
        t_arr.append(t)
    context={
        'map':m._repr_html_(),
        'times':t_arr
    }

    return render(request, 'spot_manage.html', context) 

def bookView(request):
    if not request.user.is_authenticated:
        messages.error(request, "You have to be logged in to book a show")
        return redirect('login')

    if request.method=="POST":
        show = Show.objects.get(id = request.POST.get('book_show'))
        show.artist = request.user
        show.save()
        

    m = folium.Map(location=(start_location[0], start_location[1]), zoom_start=13)
    for s in Spot.objects.all():
        print('adding '+ s.name +' at: ' + str(s.lan)+'; '+  str(s.lon))
        marker = folium.Marker(
            location=[+s.lan, +s.lon],
            tooltip="Zobrazit informace",
            popup=f"""<b>{s.name}</b><br><small>{s.description}</small><br><button class='btn btn-primary' onclick='loadShows(this)' id='{s.id}'>Rezervovat</button>""",
            icon=folium.Icon(color="blue", icon="music")
        )
        
        marker.add_to(m)

    m.get_root().html.add_child(JavascriptLink('../static/js/show_book_iframe.js'))

    times = TimeSlot.objects.all()

    context={
        'map':m._repr_html_(),
        'times':times
    }
    return render(request, 'show_book.html', context)

def showView(request):
    if not request.user.is_authenticated:
        messages.error(request, "You have to be logged in to manage your shows")

    if request.method == "POST": 
        try:
            show = Show.objects.get(id=request.POST.get('del'))
            show.artist = None
            show.save()
        except:
            print('error')
            messages.error(request, "There was an error deleting your booking")

    s = Show.objects.filter(artist=request.user)
    context = {
        'shows':s
    }
    return render(request, 'my_shows.html', context)

def showList(request):
    if request.method == "POST":
        try:
            m = Feedback.objects.create(
                show=Show.objects.get(id=request.POST.get('id')),
                email=request.POST.get('email'),
                body=request.POST.get('message')
            )
            messages.success(request, message="Vaše zpráva byla úspěšně odeslána")
        except Exception as e:
            print('There was an error creating the message: ' + str(e))

    shows = Show.objects.filter(artist__isnull=False)
    context= {
        'shows':shows
    }
    return render(request, 'show_list.html', context)

def feedback(request):
    if not request.user.is_staff:
        messages.error(request, "K přístupu na tuto stránku nemáte dostatečná oprávnění")
        return redirect('home')
    f = Feedback.objects.all()
    f_old = f.filter(seen=True)
    f = f.filter(seen=False)
    context = {
        'f':f,
        'f_old':f_old,
    }
    return render(request, 'feedback_list.html', context)

def feedbackView(request, pk):
    if not request.user.is_staff:
        messages.error(request, "K přístupu na tuto stránku nemáte dostatečná oprávnění")
        return redirect('home')
    try:
        f = Feedback.objects.get(id=pk)
        f.seen = True
        f.save()
    except:
        messages.error("Couldn't find the requested message")
        return redirect('feedback')
    context = {
        'f':f
    }
    return render(request, 'feedback_view.html', context)

def artistView(request, pk):
    try:
        a = User.objects.get(id=pk)
        profile = UserProfile.objects.get(user=a)
        fb = Feedback.objects.filter(show__artist = a)
    except:
        messages.error(request, "We couldn't find the requested user")
        return redirect('home')
    context = {
        'artist':a,
        'profile':profile,
        'feedback':fb
    }
    return render(request, 'artist_view.html', context)

def artistOverview(request):
    if not request.user.is_staff:
        messages.error(request, "K přístupu na tuto stránku nemáte dostatečná oprávnění")
        return redirect('home')
    artists = User.objects.filter(is_staff=False)
    context = {
        'artists':artists
    }
    return render(request, 'artist_overview.html', context)