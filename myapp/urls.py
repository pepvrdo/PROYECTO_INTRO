from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('respiracion/', views.respiracion, name='Respira'),
    path('about/', views.about, name='about'),
    path('home0/', views.noauth, name='home0'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("logout/", views.signout, name="logout"),
    path('new_user/', views.new_user, name='new_user'),
    path('qr-code/', views.qr_code, name='qr_code'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('download-qr/', views.download_qr, name='download_qr'),
    path("saber_mas/", views.info, name="saber_mas" ),
    path("tutorial/", views.tut, name="tutorial"),
    path('ejemplos/', views.ejemplos, name='ejemplos')
]
