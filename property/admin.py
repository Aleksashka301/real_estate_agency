from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'normalized_phone')
    search_fields = ('full_name',)
    raw_id_fields = ('flats',)


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
