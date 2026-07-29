from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='user-create'),
    path('<int:userId>/wallet/', views.WalletCreateView.as_view(), name='wallet-create'),
    path('<int:userId>/balance/', views.UserBalanceView.as_view(), name='user-balance'),
    path('<int:userId>/transactions/', views.UserTransactionsView.as_view(), name='user-transactions'),
]