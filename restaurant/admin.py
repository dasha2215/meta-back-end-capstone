from django.contrib import admin
from .models import Booking, Menu

# Register with the custom admin class
admin.site.register(Booking)
admin.site.register(Menu)
