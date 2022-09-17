from importlib.resources import path
from django.urls import path
from coaching.views import home, logout_user, register_user

app_name = "coaching"

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

]
