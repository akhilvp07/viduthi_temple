from django.shortcuts import render, redirect

def redirect_to_app(request):
    return redirect('temple_app:temple')