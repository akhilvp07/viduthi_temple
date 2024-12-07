from django.contrib import admin
from .forms import Eventform
from .models import Event

# Define the EventAdmin class
class EventAdmin(admin.ModelAdmin):
    form = Eventform  # Use the custom form defined in forms.py
    list_display = ('name', 'description')  # Display fields in the admin list view
    search_fields = ('name',)  # Add search functionality for event names

# Register the Event model with the custom admin interface
admin.site.register(Event, EventAdmin)
