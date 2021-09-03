from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'World'
    return render(request, 'learndjango/main.html', {'name': name})
