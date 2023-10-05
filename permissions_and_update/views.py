from django.shortcuts import render

def home(request):
    return render(request, 'permissions_and_update/home.html')
