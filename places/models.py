from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')

    lat = models.FloatField('Ширина')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name = 'Интересные места'


class Photo(models.Model):
    image = models.ImageField('Изображение', upload_to='images', null=True)
    sort_index = models.PositiveSmallIntegerField(
        'Порядковый номер',
        default=0,
    )

    place = models.ForeignKey(
        Place,
        related_name='place_photos',
        verbose_name='Место',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['sort_index']

    def __str__(self):
        return f'{self.sort_index} {self.place.title}'
