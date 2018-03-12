from django.contrib import admin
from .models import Holiday, LeaveInfo


class LeaveInfoInline(admin.TabularInline):
    model = LeaveInfo
    extra = 1


class HolidayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['HolidayName']}),
        ('Holiday ID', {'fields': ['HolidayID']}),
        ('Holiday Start Date', {'fields': ['HolidayStartDate'], 'classes': ['collapse']}),
        ('Holiday End Date', {'fields': ['HolidayEndDate'], 'classes': ['collapse']}),
    ]
    inlines = [LeaveInfoInline]


admin.register(Holiday, LeaveInfo)
