from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo



def photo_list(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "map/photo.html", context)
