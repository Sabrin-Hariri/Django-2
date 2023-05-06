
from django.urls import path
from . import views 
from django.contrib.auth import views as authViews 
from .views import * 

########################################


urlpatterns = [

    # path('<int:number1>/<int:number2>', views.student , name='student')
    # path('', views.student , name='student'),
    path('', HomePage.as_view() , name='student'),
    path('add/', views.Add , name='add'),
    path('edit/', views.Edit , name='edit'),
]