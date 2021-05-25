from django.shortcuts import render

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
