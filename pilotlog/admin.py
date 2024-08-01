from django.contrib import admin
from .models import Aircraft


class AircraftAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'guid', 'active', 'record_modified')
    list_filter = ('active', 'make', 'category', 'class_type')
    search_fields = ('make', 'model', 'guid', 'reference')
    fieldsets = (
        ('Basic Info', {
         'fields': ('make', 'model', 'sub_model', 'guid', 'user_id')}),
        ('Classification', {
         'fields': ('class_type', 'category', 'power', 'seats')}),
        ('Status', {'fields': ('active', 'fav_list',
         'complex', 'high_perf', 'aerobatic', 'tailwheel')}),
        ('Technical Details', {
         'fields': ('efis', 'fnpt', 'run2', 'kg5700', 'cond_log')}),
        ('Reference', {'fields': ('ref_search',
         'reference', 'company', 'rating')}),
        ('Defaults', {'fields': ('default_app', 'default_log',
         'default_ops', 'default_launch', 'device_code', 'aircraft_code')}),
        ('Modification Info', {'fields': ('record_modified',)}),
    )


admin.site.register(Aircraft, AircraftAdmin)
