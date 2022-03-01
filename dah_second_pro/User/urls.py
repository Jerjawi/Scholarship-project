from django.urls import path
from .views import regirster, start_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('register/',regirster, name = 'register'),
    path('login/',auth_view.LoginView.as_view(template_name = 'User/login.html'), name = 'login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'User/logout.html'), name = 'logout'),
    path('start_view/', start_view, name = 'start_view')

]