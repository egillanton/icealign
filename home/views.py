from django.shortcuts import render

def home(request):
    context_dir = {"title": ""}
    return render(request, 'home/home.html', context=context_dir)
