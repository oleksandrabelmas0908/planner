from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),

]