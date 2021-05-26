from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Photo


class PhotoInline(admin.TabularInline):
    model = Photo

    readonly_fields = ('image_preview', )
    fields = ('image', 'image_preview', 'sort_index')

    def image_preview(self, obj, width=200):
        return format_html('<img src={} width={}/>', obj.image.url, width)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo)
