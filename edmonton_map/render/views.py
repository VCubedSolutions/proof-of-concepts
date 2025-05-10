from django.http import HttpResponse
import os
from django.shortcuts import render

# Create your views here.
def index(request):
    CESIUM_API_KEY = os.getenv("CESIUM_API_KEY")
    return render(request, "render/index.html", {"CESIUM_API_KEY": CESIUM_API_KEY})

def cesium_token(request):
    CESIUM_API_KEY = os.getenv("CESIUM_API_KEY") or ''
    return HttpResponse(CESIUM_API_KEY.encode(), content_type="text/plain")
