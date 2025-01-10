# from django.shortcuts import render 
# from django.http.response import JsonResponse
# from .forms import EventForm

# Create your views here.
# def index(request):
#     festival = ['Festival A', 'Festival B', 'Festival C']
#     return render(request=request, template_name='temple/index.html', context={'data':festival})

def about(request):return render(request=request, template_name='temple/about.html')

# def add_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             event_name = form.cleaned_data['event_name']
#             event_description = form.cleaned_data['event_description']
#             # Handle the data, e.g., save to the database
#             print(event_name, event_description)
#     else:
#         form = EventForm(initial={'event_name': 'hi', 'event_description': 'string'})

#     return render(request, 'temple/add_event.html', {'form': form})

import os
from django.conf import settings
from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    # Festivals data
    festival = ['Festival A', 'Festival B', 'Festival C']
    
    # Images data
    try:
        images_dir = os.path.join(settings.BASE_DIR, 'static/images')
        images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    except FileNotFoundError:
        images = []  # Fallback if the directory doesn't exist

    # Context data
    context = {
        'data': festival,
        'images': images,
    }
    
    return render(request, 'temple/index.html', context)

# API Endpoint for Images (Optional)
def fetch_images(request):
    try:
        images_dir = os.path.join(settings.BASE_DIR, 'static/images')
        images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        return JsonResponse({'images': images}, status=200)
    except FileNotFoundError:
        return JsonResponse({'error': 'Image directory not found'}, status=404)
