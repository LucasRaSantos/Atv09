from django.shortcuts import render

def home_menu(request):
    return render(request, 'index.html')
