from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'World'
    return render(request, 'blog/index.html', {'name': name})