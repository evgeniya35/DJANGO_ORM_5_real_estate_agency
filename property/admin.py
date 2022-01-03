from django.contrib import admin

from .models import Flat, Likes

class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)

admin.site.register(Flat, FlatAdmin)

class LikesAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Likes, LikesAdmin)
