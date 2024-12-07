from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Eventform
from .models import Event

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if the user is a superuser (admin privileges)
            if user.is_superuser:
                login(request, user)
                return redirect('temple_admin:admin_dashboard')  # Redirect to the admin dashboard
            else:
                messages.error(request, "You do not have the necessary permissions.")
        else:
            messages.error(request, "Invalid credentials.")
    
    return render(request, 'temple_admin/login.html')

@login_required
def admin_dashboard(request):
    # Your admin dashboard logic here
    return render(request, 'temple_admin/admin_dashboard.html')


@login_required
def add_festival(request):
    if request.method == 'POST':
        form = Eventform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = Eventform
    
    return render(request,'temple_admin/add_festival_modal.html', {'form': form})

@login_required
def post_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_details = request.POST.get('event_description')
        print(event_name, event_details)
        event = Event(name=event_name,description=event_details)
        event.save()
        events = Event.objects.all()
        for event in events:
            print(event.name, event.description)
        
    return redirect('temple_admin:admin_dashboard')