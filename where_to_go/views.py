from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
                    'detailsUrl': reverse('place-detail', args=[place.id]),
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

    place_metadata = {
        'title': place.title,
        'imgs': [photo.image.url for photo in place.place_photos.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lon': place.lon,
        }
    }

    return JsonResponse(place_metadata, json_dumps_params={'ensure_ascii': False, 'indent': 2})
