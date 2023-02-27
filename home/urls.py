from django.urls import path

from . views import LogoutUSer,LoginUSer,HomeListView,HomeDetailView,CreateView,DeleteView,UpdateView

app_name = 'home'

urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('<int:pk>/',HomeDetailView.as_view(),name='detail'),
    path('create/',CreateView.as_view(),name='car_create'),
    path('delete/<int:pk>/',DeleteView.as_view(),name='car_delete'),
    path('update/<int:pk>/',UpdateView.as_view(),name='car_update'),
    path('login/',LoginUSer.as_view(),name='login'),
    path('logout/',LogoutUSer.as_view(),name='logout'),


]