from django.urls import path
from .views import home, login_view,admin_view,register_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin_view, name='admin'),  # Add admin view if needed
    path('register/',register_view, name='register'),

]
