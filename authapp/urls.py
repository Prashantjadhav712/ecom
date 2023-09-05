from django.urls import path,include
from authapp import views as v

urlpatterns = [
    path("signup/",v.signup,name="signup"),
    path("login/",v.handlelogin,name="handlelogin"),
    path("logout/",v.handlelogout,name="handlelogout"),
    path('activate/<uidb64>/<token>/',v.ActivateAccountView.as_view(),name="activate")


]



  