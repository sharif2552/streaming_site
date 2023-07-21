from django.shortcuts import render, HttpResponse
from .models import video

# Create your views here.
def home(request):
    items = video.objects.all()
    return render(request, 'index.html', {'items': items})

def details(request, id):
    if id is not None:
        item = video.objects.get(id=id)
        return render(request, 'details.html', {'item': item})
    else:
        return HttpResponse("Error")