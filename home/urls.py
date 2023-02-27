from django.urls import path

from . views import HomeListView,HomeDetailView,CreateCarView

app_name = 'home'

urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('<int:pk>/',HomeDetailView.as_view(),name='detail'),
    path('create/',CreateCarView.as_view(),name='car_create'),


]