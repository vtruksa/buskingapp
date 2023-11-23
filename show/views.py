from django.shortcuts import render

import folium, clipboard

# Create your views here.
def manageSpots(request):
    m = folium.Map(location=(50.0755, 14.4378))
    #m.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=False))
    m.add_child(folium.ClickForMarker(popup="<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}<br><button class='btn btn-primary'>Přidat</button>"))

    context={
        'map':m._repr_html_()
    }

    return render(request, 'spot_manage.html', context)