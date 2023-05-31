from django.urls import path
from lkapp import views

urlpatterns = [
    path('LaptopKinboApi/', views.api_list),
]