from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import logout

def landing_view(request):
    return render(request, 'others/landing-page.html')

@login_required
def profile_view(request):
    return render(request, 'account/user-profile.html')

def custom_logout(request):
    logout(request)
    return redirect('landing')
