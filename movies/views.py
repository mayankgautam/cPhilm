from cPhilm.engine import playable_path
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from movies.models import *
import subprocess

def index(request):
    return render(request, 'list.html', {'title': 'Movies', 'items': Movie.objects.filter(watched=False)})

