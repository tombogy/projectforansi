from django.urls import path
from . import views

urlpatterns = [
    path("",views.register,name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("home/",views.home,name="home"),
    path("add/",views.add_item,name="add"),
    path("edit/",views.edit_item,name="edit"),
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    path("delete/<int:id>/",views.delete_item,name="delete"),
    path("category/",views.category,name="category"),
    path("trip/",views.trip,name="trip"),
    path("point/",views.point,name="point"),
    path("password/",views.password,name="password"),
    path("vehicle/",views.vehicle,name="vehicle"),
    path("driver/",views.driver,name="driver"),
    path("home2/",views.home2,name="home2"),
    path("add_d/",views.add_d,name="add_d"),
    path('registration/', views.driver_registration, name='registration'),
    
    ] 


