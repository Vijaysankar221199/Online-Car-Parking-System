from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from datetime import datetime
from django.conf import settings



class scanupload(models.Model):
    CHOICES = (
        ('allow', 'Allow'),
        ('occupied', 'Occupied'),
    )
    id = models.AutoField(primary_key=True)
    slot_name = models.CharField(max_length=50, blank=True, null=True)
    visiname = models.CharField(max_length=50, blank=True, null=True, default="NONE")
    date = models.DateTimeField(default=datetime.now, blank=True)
    status =  models.CharField(max_length=50, choices= CHOICES, blank=True, default = "allow")
    car_number = models.CharField(max_length=50, blank=True, null=True)
    Phonenumber = models.CharField(max_length=30, blank=True)


from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user =  models.CharField(max_length=50, blank=True, null=True)
    car_number = models.TextField(max_length=500, blank=True)
    Phonenumber = models.CharField(max_length=30, blank=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class otp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    otp = models.CharField(max_length=5, blank=True, null=True)
    visiname = models.CharField( max_length=5, blank=True, null=True)
