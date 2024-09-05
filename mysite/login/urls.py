from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('protegida/', views.pagina_protegida, name='pagina_protegida'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),  # Asegúrate de que el nombre sea 'login'
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
