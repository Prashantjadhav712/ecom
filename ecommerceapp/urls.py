from django.urls import path,include
from .import views as v

urlpatterns = [
    path("",v.index,name="index"),
    path("contact",v.contact,name="contact"),
    path("about",v.about,name="about"),
    path('checkout',v.checkout,name="checkout"),
    path('handlerequest',v.handlerequest,name="handlerequest")
]