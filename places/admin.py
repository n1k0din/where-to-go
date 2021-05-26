from django.contrib import admin

from .models import Place, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo)
