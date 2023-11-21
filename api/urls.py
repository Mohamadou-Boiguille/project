from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin_view, name='api-signin'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.session_view, name='api-session'),
    path('whoami/', views.whoami_view, name='api-whoami'),
    path('tournaments/', views.tournaments_view, name='api-tournaments'),
]
