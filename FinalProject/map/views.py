from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo



def photo_list(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "map/photo.html", context)

def record(request):
	return  render(request, "map/record.html", context)

def diary(request):
        return  render(request, "map/diary.html", context)
