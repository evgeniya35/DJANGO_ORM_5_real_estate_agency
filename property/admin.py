from django.contrib import admin

from .models import Flat, Likes, Owner

class OwnerInLine(admin.TabularInline):
    model = Owner.flat.through
    extra = 3
    raw_id_fields = ('owner',)

class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    inlines = (OwnerInLine,)

admin.site.register(Flat, FlatAdmin)

class LikesAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Likes, LikesAdmin)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone',]

admin.site.register(Owner, OwnerAdmin)
