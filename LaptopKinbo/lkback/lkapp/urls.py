from django.urls import path
from lkapp import views

urlpatterns = [
    path('laptop/kinbo/api/', views.api_list),
    path('laptopdetails/<int:pk>/', views.api_detail),
    path('laptopinrange/<int:l>/<int:h>/', views.laptops_list),

]