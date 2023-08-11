from django.urls import path
from company.views import manage_company_views as views

urlpatterns = [
    path('companies/', views.company_list, name='company-list'),
    
    path('companies/<int:pk>/', views.company_detail, name='company-detail'),

]
