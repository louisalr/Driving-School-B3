from django.db import models
from django.contrib.auth.models import User, AbstractUser


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    description = models.TextField(max_length=255, null=True, blank=True)


class Customer(AbstractUser):
    isManager = models.BooleanField(default=False)
    school = models.ManyToManyField(School)

    def save(self, *args, **kwargs):
        self.username = f"{self.first_name}{self.last_name}"
        super(Customer, self).save(*args, **kwargs)


class Booking(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
