from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    )
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return f"{self.username}"