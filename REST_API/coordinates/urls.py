from django.urls import path

from .views import CoordinatesView


app_name = "coordinates"


urlpatterns = [
    path('coordinates/', CoordinatesView.as_view()),
    path('coordinates/<int:pk>', CoordinatesView.as_view()),
]
