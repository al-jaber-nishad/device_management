from django.urls import path
from devices.views import manage_device_views as views
urlpatterns = [
    path('devices/', views.device_list, name='device-list'),
    
    path('devices/<int:pk>/', views.device_detail, name='device-detail'),

    path('devices/check_out/', views.device_check_out, name='device-check-out'),

    path('devices/check_in/', views.device_check_in, name='device-check-in'),

]
