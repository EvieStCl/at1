#view for splash page
from django.shortcuts import render

def splash_page(request):
    return render(request, 'splash/splash_page.html')