from django.urls import path
from . import views

urlpatterns = [
    path('api/signup/', views.UserCreate.as_view(), name='user-create'),
    path('api/login/', views.UserLogin.as_view(), name='user-login'),
    path('api/logout/', views.UserLogout.as_view(), name='user-logout'),
]
