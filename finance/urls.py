from django.urls import path
from . import views

urlpatterns = [
    path('api/get_access_token/', views.get_access_token.as_view(),
         name='get-access-token'),
]
