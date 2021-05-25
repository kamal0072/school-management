from django.urls import path
from . import  views

urlpatterns = [
    path('',views.homeview,name='studform'),
    path('map/',views.default_map,name="default"),
]

