from django.contrib import admin

from .models import Flat, Likes, Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flat.through
    extra = 3
    raw_id_fields = ('owner',)
    classes = ('collapse',)


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('created_at', 'price', 'active', 'new_building', 'liked_by')}),
        ('Расположение', {'classes': ('collapse',), 'fields': ('town', 'town_district', 'address',)}),
        ('Описание объекта', {'classes': ('collapse',), 'fields': ('floor', 'rooms_number', 'living_area', 'has_balcony', 'construction_year', 'description',)}),
    )
    inlines = (OwnerInLine,)


class LikesAdmin(admin.ModelAdmin):
    list_display = ('author', 'flat',)
    raw_id_fields = ('flat', 'author')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone',]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Likes, LikesAdmin)
