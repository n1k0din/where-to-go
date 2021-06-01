from io import BytesIO

import requests
import urllib3
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile

from places.models import Place, Photo


class Command(BaseCommand):
    help = 'Load place from URL'

    def add_arguments(self, parser):
        parser.add_argument('place_urls', nargs='+')

    def handle(self, *args, **options):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        for place_url in options['place_urls']:
            response = requests.get(place_url, verify=False)
            response.raise_for_status()

            place_metadata = response.json()

            place, _place_created = Place.objects.update_or_create(
                title=place_metadata['title'],
                defaults={
                    'description_short': place_metadata['description_short'],
                    'description_long': place_metadata['description_long'],
                    'lat': place_metadata['coordinates']['lat'],
                    'lon': place_metadata['coordinates']['lng'],
                },
            )

            for num, img_url in enumerate(place_metadata['imgs']):

                photo, _photo_created = Photo.objects.get_or_create(
                    sort_index=num,
                    place=place,
                )

                response = requests.get(img_url, verify=False)
                response.raise_for_status()

                image = ImageFile(BytesIO(response.content))

                photo.image.save(f'{place.id}_{photo.id}.jpg', image, save=True)
