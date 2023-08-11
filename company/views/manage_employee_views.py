from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from company.models import Employee, Company
from company.serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        companies = Employee.objects.all()
        serializer = EmployeeSerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_employee_to_company(request, company_pk, employee_pk):
    company = get_object_or_404(Company, pk=company_pk)
    employee = get_object_or_404(Employee, pk=employee_pk)
    
    if company and employee:
        employee.company = company
        employee.save()
        return Response({'message': f'Employee {employee.user.username} added to company {company.name}'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)