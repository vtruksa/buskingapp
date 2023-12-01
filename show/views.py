from django.shortcuts import render
from django.contrib import messages
from branca.element import JavascriptLink

from .models import *

import folium, clipboard

alltimes = ['10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00', '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00', '14:00-14:30', '14:30-15:00', '15:00-15:30', '15:30-16:00', '16:00-16:30', '16:30-17:00', '17:00-17:30', '17:30-18:00', '18:00-18:30', '18:30-19:00', '19:00-19:30', '19:30-20:00', '20:00-20:30', '20:30-21:00', '21:00-21:30', '21:30-22:00']

start_location = [50.0755, 14.4378]

def manageSpots(request):
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
        print(show)
        

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

    context={
        'map':m._repr_html_(),
    }
    return render(request, 'show_book.html', context)