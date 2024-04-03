from django.shortcuts import render

def splash_page(request):
    return render(request, 'at1/splash.html')

def dashboard_page(request):
    # Redirect to the dashboard page after login
    if request.user.is_authenticated:
        return render(request, 'at1/dashboard.html', {'user': request.user})
    else:
        # Redirect to the login page if not authenticated
        return redirect('login')