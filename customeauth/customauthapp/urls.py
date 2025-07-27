from django.urls import path
from .views import email_login_view, Register_view, admin_dashboard_view, homepage,logout_view,user_dashboard_view
from customauthapp.contactform import contactform_view
from customauthapp.password_reset import password_reset
from customauthapp.new_password import new_password

#app_name='customauthapp'
urlpatterns = [
    path('login/', email_login_view, name='login'),
    path('register/', Register_view, name='register'),
    path('admindashboard/',admin_dashboard_view, name='admindashboard'),
    path('user_dashboard/', user_dashboard_view, name='user_dashboard'),
    path('',homepage, name='home'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', password_reset, name='password_reset'),
    path('new-password/<uuid:unique_id>/user/<str:email>/user_is/<int:pk>/', new_password, name='new-password'),
    path('contact/', contactform_view, name='contact'),

]
