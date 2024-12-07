from django.shortcuts import render 
from django.http.response import JsonResponse
#from .forms import EventForm

# Create your views here.
def index(request):
    festival = ['Festival A', 'Festival B', 'Festival C']
    return render(request=request, template_name='temple/index.html', context={'data':festival})

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
    