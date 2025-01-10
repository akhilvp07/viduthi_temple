from django.urls import path
from .views import *

app_name = 'temple_admin'

urlpatterns = [
    path('',view=admin_login, name='temple_admin'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/post_event/', post_event, name='post_event'),
    ]