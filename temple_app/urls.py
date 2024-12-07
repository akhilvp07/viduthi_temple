from django.urls import path  
from . import views
app_name = 'temple_app'

urlpatterns = [
    path('',view=views.index, name='temple'),
   # path('add-event/',views.add_event, name='add_event'),
    path('about/',view=views.about,name='about'),
    path('fetch-images/', views.fetch_images, name='fetch_images'), 

]