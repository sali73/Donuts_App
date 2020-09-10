
from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('', views.Home , name= 'home'),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),


]

