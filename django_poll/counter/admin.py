from django.contrib import admin
from counter.models import Segment, Guest


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1
    
    
class SegmentAdmin(admin.ModelAdmin):
    inlines = [GuestInline]


admin.site.register(Segment, SegmentAdmin)