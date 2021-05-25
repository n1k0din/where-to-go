from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')

    lat = models.FloatField('Ширина')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.title}'


class Photo(models.Model):
    image = models.ImageField('Изображение', upload_to='images', null=True, blank=True)
    sort_index = models.SmallIntegerField(
        'Порядковый номер',
        default=1,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(1),
        ]
    )

    place = models.ForeignKey(
        Place,
        related_name='place_photos',
        verbose_name='Место',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.sort_index} {self.place.title}'
