from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    description = models.TextField(max_length=255, null=True, blank=True)
    picture_url = models.URLField(null=True, blank=True)


class Customer(AbstractUser):
    isManager = models.BooleanField(default=False)
    school = models.ManyToManyField(School)

    def save(self, *args, **kwargs):
        # Generate a random username based on a uuid
        if self.is_superuser:
            self.username = uuid.uuid1()
        # Else, user comes from the form, so we use his first and last name
        else:
            self.username = f"{self.first_name}{self.last_name}"
            super(Customer, self).save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(School, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Customer, related_name='attended_events')
    max_attendees = models.IntegerField()
    date = models.DateField()
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()

    def add_attendee(self, user):
        if self.attendees.count() < self.max_attendees:
            self.attendees.add(user)
            return True
        else:
            return False
