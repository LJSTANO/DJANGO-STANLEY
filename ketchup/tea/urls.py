

from django.urls import path
from.import views

app_name = "tea"
urlpatterns =[
    path('', views.index, name='home'),



]