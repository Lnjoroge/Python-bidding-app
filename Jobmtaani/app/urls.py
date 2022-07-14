from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('registerUser/', views.register_user, name='register_user'),
    path('registerClient/', views.register_client, name='register_client'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('client/', views.client, name='client'),


    path('', views.home, name='home'),
    
    path('marketplace/', views.placements, name='placements'),
    path('marketplace/<placement_slug>/', views.placement_detail, name='placement-detail'),

    path('my-bids/', views.bid_summary, name='bid-summary' ),
    path('confirm-bids/', views.confirm_bids, name='confirm-bids'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about')

]
