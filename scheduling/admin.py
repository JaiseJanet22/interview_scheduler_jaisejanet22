from django.contrib import admin
from .models import User, Availability

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_type')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_time', 'end_time', 'date')
