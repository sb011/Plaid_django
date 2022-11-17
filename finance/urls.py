from django.urls import path
from . import views

urlpatterns = [
    path('api/get_access_token/', views.get_access_token.as_view(),
         name='get-access-token'),
    path('api/get_transactions/',
         views.get_transaction.as_view(), name='get-transaction'),
    path('api/identity/', views.get_identity.as_view(), name='get-identity'),
    path('api/balance/', views.get_balance.as_view(), name='get-balance'),
    path('api/item/', views.get_item_info.as_view(), name='get-item-info'),
    path('api/accounts/', views.get_balance.as_view(), name='get-balance'),
    path('api/webhook/', views.webhook, name='webhook'),
]
