from importlib.resources import path
from django.urls import path
from coaching.views import home, logout_user, register_user, login, process

app_name = "coaching"

urlpatterns = [
    path('', home, name='home'),
    path('process/', process, name='process'),
    path('logout/', logout_user, name='logout'),
    path('profile/', home, name='profile'),
    path('login/', login, name='login'),
    path('register/', register_user, name='register'),

]
