from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),

    path('services/', views.services, name='services'),

    path('insert_data/', views.insert_data, name='insert_data'),

    path('data/', views.view, name='data_view'),
]

# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)