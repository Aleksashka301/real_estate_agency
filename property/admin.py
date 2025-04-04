from django.contrib import admin
from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'owners_phonenumber', 'owner_pure_phone')
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('likes',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
