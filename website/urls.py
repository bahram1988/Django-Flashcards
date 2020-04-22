from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Add.html', views.Add, name='Add'),
    path('Subtract.html', views.Subtract, name='Subtract'),
    path('Multiply.html', views.Multiply, name='Multiply'),
    path('Divide.html', views.Divide, name='Divide'),    

]