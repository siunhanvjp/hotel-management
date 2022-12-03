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
    path('update_booking_all/<pk>', views.update_booking_all, name="update_booking_all"),
    path('update_booking_future/<pk>', views.update_booking_future, name="update_booking_future"),
]
