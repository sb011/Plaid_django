from django.urls import path
from . import views

urlpatterns = [
    path('api/get_access_token/', views.get_access_token.as_view(),
         name='get-access-token'),
    path('api/get_transactions/',
         views.get_transaction.as_view(), name='get-transaction'),
    path('api/identity/', views.get_identity.as_view(), name='get-identity'),
]
