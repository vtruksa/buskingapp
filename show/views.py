from django.shortcuts import render
from branca.element import JavascriptLink

import folium, clipboard

# Create your views here.
def manageSpots(request):
    m = folium.Map(location=(50.0755, 14.4378))
    #m.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=False))
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