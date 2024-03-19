from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=False, unique=True)
