from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('booking/<str:pk>', views.view_booking, name="view_booking"),
    path('addroomtype/', views.addroomtype, name="addroomtype"),
    path('statistic/', views.statistic, name="statistic"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
