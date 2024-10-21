from django.urls import path
from customer.views import *
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('forgetpw', forgetpw, name='forgetpw'), 
    path('otp', otp, name='otp'),
    path('newpw', newpw, name='newpw'),
    path('changepw', changepw, name='changepw'),
    path('display_profile', display_profile, name='display_profile')
]
