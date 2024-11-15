from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('home/', views.home, name='home'),
    path('respiracion/', views.respiracion, name='Respira'),
    path('about/', views.about, name='about'),
    path('home0/', views.noauth, name='home0'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("logout/", views.signout, name="logout")
]
