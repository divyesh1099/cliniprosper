from django.urls import path
from . import views
app_name='home'
urlpatterns=[
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.custom_login, name='login'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('new_password', views.new_password, name='new_password'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
]
