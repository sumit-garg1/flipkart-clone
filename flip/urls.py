from django.contrib import admin
from django.urls import path
# from home import views
from flip import views
urlpatterns = [
    path('',views.index,name="home"),
    path('login/',views.loginUser,name="login"),
    # path('logout',views.logout,name="logout")
    path('contact',views.Contact, name="contact"),
    path('cart',views.cart, name="cart")
]