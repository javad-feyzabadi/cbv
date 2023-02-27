from django.shortcuts import render
from django.views import View
from django.views.generic import (UpdateView,ListView,DetailView,
                                  FormView,TemplateView,
                                  CreateView,DeleteView,
                                  MonthArchiveView
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView

from rest_framework.generics import ListAPIView,RetrieveAPIView

from . models import Car
from . serializers import CarSerializer
# from . forms import CarCreateForm



class Home(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class SingleCar(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
































# class HomeListView(ListView):
#     template_name = 'home/home.html'
#     model = Car

# class HomeDetailView(DetailView):
#     model = Car


# class CreateCarView(FormView):
#     template_name = 'home/create.html'
#     form_class = CarCreateForm
#     success_url = reverse_lazy('home:home')

    
#     def form_valid(self, form):
#         self._create_car(form.cleaned_data)
#         messages.success(self.request,'create car successfully','success')
#         return super().form_valid(form)
    
#     def _create_car(self,data):
#         Car.objects.create(name = data['name'],owner = data['owner'],year = data['year'])


# class CreateView(CreateView):
#     model = Car
#     fields = ['name' , 'year']
#     template_name = 'home/create.html'
#     success_url = reverse_lazy('home:home')

#     def form_valid(self, form ):
#         car = form.save(commit=False)
#         car.owner = self.request.user.username if self.request.user.username else 'nothing'
#         car.save()
#         messages.success(self.request,'create car successfully','success')
#         return super().form_valid(form)


# class DeleteView(DeleteView):
#     model = Car
#     success_url = reverse_lazy('home:home')
#     template_name = 'home/delete.html'

# class UpdateView(UpdateView):
#     model = Car
#     success_url = reverse_lazy('home:home')
#     fields = ['name','year']
#     template_name = 'home/update.html'

# class LoginUSer(LoginView):
#     template_name= 'home/login.html'
    
# class LogoutUSer(LogoutView):
#     pass

# class MounthCar(MonthArchiveView):
#     model = Car
#     date_field = 'created'
#     template_name = 'home/home.html'
#     context_object_name = 'cars'  #object_list  => default
#     month_format = '%m'




# class Home(TemplateView):
#      template_name = 'home/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cars'] = Car.objects.all()
#         return context

    # http_method_names=['get','options']

    # def get(self,request):
    #     return render(request,'home/home.html')

    # def options(self, request, *args, **kwargs):
    #     response = super().options(request, *args, **kwargs)
    #     response.headers['host']='localhost'
    #     response.headers['user']=request.user
    #     return response

    # def http_method_not_allowed(self, request, *args, **kwargs):
    #     return render(request,'method_not_allowed.html') 