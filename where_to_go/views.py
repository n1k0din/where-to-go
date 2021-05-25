from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from places.models import Place


def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lon, place.lat],
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': 'static/places/moscow_legends.json',
                }
            }
        )

    context = {
        'geojson_places': {
            'type': 'FeatureCollection',
            'features': features,
        }
    }

    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return HttpResponse(place.title)
