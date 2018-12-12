from django.db import models
from djangae import fields

class UsedNumber(models.Model):
    number = fields.CharField()

    def __str__(self):
        return self.number
