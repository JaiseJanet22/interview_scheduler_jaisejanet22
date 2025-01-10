from django.urls import path
from .views import RegisterAvailability, GetAvailableSlots

urlpatterns = [
    path('register/', RegisterAvailability.as_view(), name='register_availability'),
    path('slots/', GetAvailableSlots.as_view(), name='get_available_slots'),
]
