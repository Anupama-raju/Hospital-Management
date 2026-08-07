from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('doctors',views.doctors,name='doctors'),
    path('department',views.department,name='dept'),
    path('doctors_list',views.doctors_list,name='doctors_list'), # - new
    path('weather',views.weather,name='weather'), # -- new
]
