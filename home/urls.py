from django.urls import path

from . views import (MounthCar,LogoutUSer,
                    LoginUSer,HomeListView,
                    HomeDetailView,CreateView,
                    DeleteView,UpdateView,MounthCar,
                    Home,SingleCar
)

app_name = 'home'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('<int:pk>/',SingleCar.as_view(),name='singel'),

    # path('',HomeListView.as_view(),name='home'),
    # path('<int:pk>/',HomeDetailView.as_view(),name='detail'),
    # path('create/',CreateView.as_view(),name='car_create'),
    # path('delete/<int:pk>/',DeleteView.as_view(),name='car_delete'),
    # path('update/<int:pk>/',UpdateView.as_view(),name='car_update'),
    # path('login/',LoginUSer.as_view(),name='login'),
    # path('logout/',LogoutUSer.as_view(),name='logout'),
    # path('<int:year>/<int:month>',MounthCar.as_view(),name='mounth'),


]