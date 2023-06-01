from django.urls import path
from lkapp import views

urlpatterns = [
    path('laptop/kinbo/api/', views.api_list),
    path('laptopdetails/<int:pk>/', views.api_detail),
    path('laptopinrange/<int:l>/<int:h>/', views.laptops_list),
    path('gaminglaptop/<int:l>/<int:h>/', views.api_game),
    path('mac/<int:l>/<int:h>/', views.mac_list),

]