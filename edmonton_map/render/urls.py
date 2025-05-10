from django.urls import path

from . import views

app_name = "render"
urlpatterns = [
    path("", views.index, name="index"),
    path('cesium_token', views.cesium_token, name='cesium_token'),
]
