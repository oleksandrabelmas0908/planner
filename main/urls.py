from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='start'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),

]