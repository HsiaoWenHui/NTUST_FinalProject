from django.http import HttpResponse
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Photo

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def photo_list(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "map/photo.html", context)
