from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('booking_all/<str:pk>', views.view_booking_all, name="view_booking_all"),
    path('booking_future/<str:pk>', views.view_booking_future, name="view_booking_future"),
    path('addroomtype/', views.addroomtype, name="addroomtype"),
    path('statistic/', views.statistic, name="statistic"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
