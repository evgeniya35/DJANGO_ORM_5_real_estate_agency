from django.contrib import admin

from .models import Flat, Likes, Owner

class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)

admin.site.register(Flat, FlatAdmin)

class LikesAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Likes, LikesAdmin)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Owner, OwnerAdmin)
