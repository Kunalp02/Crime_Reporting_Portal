from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('google-oauth2/', include('social_django.urls', namespace='social')),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('newsletter/', views.newsletter, name="newsletter"),

]