"""donuts_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from api import views

app_name = 'api'
urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.Index, name='index'),
    path('home/', views.Home, name= 'home'),
    path('add/', views.AddDonuts, name='add'),
    path('add_donuts_form_submission/', views.add_donuts_form_submission , name='add_donuts_form_submission'),
    path("register/", views.register, name="register"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/login.html'), name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name='users/logout.html'), name="login"),
    path('index/<id>/', views.detail_view , name= "detail_view"),
    path('<id>/update', views.update_view , name="update_view"),
    path('<id>/delete', views.delete_view , name= "delete_view"),
    path('cart/', views.view, name="cart"),
    path('(?P<slug>[^/]+)/cart$', views.update_cart, name="update_cart"),

]

