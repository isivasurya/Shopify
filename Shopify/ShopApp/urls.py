from django.urls import path
from .views import *
from ShopApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.userlogin, name="userlogin"),
    path('logout/', views.userlogout, name="userlogout"),
    path('collections/', views.collections, name="collections"),
    path('collections/<str:cname>', views.Viewcollections, name="Viewcollections"),
    path('collections/<str:cname>/<str:pname>', views.proddtls, name="proddtls"),
]