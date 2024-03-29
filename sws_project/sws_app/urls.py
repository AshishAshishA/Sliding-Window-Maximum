from django.urls import path
from .views import get_index,sw_simulator

urlpatterns=[
    path('',get_index,name="get_index"),
    path('sw_simulator',sw_simulator,name="sw_simulator")
]