from django.db import models
from company.models import Company, Employee

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100)
    deviceID = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return f"{self.name}"


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_checked_in = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return f"{self.device.name}"