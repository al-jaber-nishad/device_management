from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from devices.models import Employee, Device, DeviceLog
from devices.serializers import DeviceSerializer, DeviceLogSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone



@api_view(['GET', 'POST'])
def device_list(request):
    if request.method == 'GET':
        companies = Device.objects.all()
        serializer = DeviceSerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def device_check_out(request):
    device_id = request.data.get('device_id')
    device = get_object_or_404(Device, pk=device_id)
    employee_id = request.data.get('employee_id')
    condition = request.data.get('condition')
    if employee_id and condition:
        employee = get_object_or_404(Employee, pk=employee_id)
        log = DeviceLog.objects.create(device=device, employee=employee, condition_when_checked_out=condition)
        return Response({'message': f'Device {device.name} checked out by {employee.user.username}', 'log_id': log.id})
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def device_check_in(request):
    device_id = request.data.get('device_id')
    device = get_object_or_404(Device, pk=device_id)
    employee_id = request.data.get('employee_id')
    condition = request.data.get('condition')
    device_log = DeviceLog.objects.filter(device=device, employee_id=employee_id, check_in_date=None).first()
    if device_log and condition:
        device_log.check_in_date = timezone.now()
        device_log.condition_when_checked_in = condition
        device_log.save()
        return Response({'message': f'Device {device.name} checked in by {device_log.employee.user.username}'})
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
