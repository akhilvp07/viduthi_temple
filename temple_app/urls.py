from django.urls import path  
from . import views
app_name = 'temple_app'

urlpatterns = [
    path('',view=views.index, name='temple'),
   # path('add-event/',views.add_event, name='add_event'),
]