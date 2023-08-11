from django.urls import path 
from company.views import manage_employee_views as views

urlpatterns = [
    path('employee/', views.employee_list, name='employee-list'),
    
    path('employee/<int:pk>/', views.employee_detail, name='employee-detail'),

    path('companies/<int:company_pk>/add_employee/', views.add_employee_to_company, name='add-employee-to-company'),
    
]
