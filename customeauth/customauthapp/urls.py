from django.urls import path
from .views import email_login_view, Register_view, dashboard_view, homepage,logout_view

#app_name='customauthapp'
urlpatterns = [
    path('login/', email_login_view, name='login'),
    path('register/', Register_view, name='register'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('',homepage, name='home'),
    path('logout/', logout_view, name='logout'),

]
