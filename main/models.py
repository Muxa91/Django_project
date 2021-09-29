from django.db import models


class clinic(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

def migrate(name, age):
    tom = clinic.objects.create(name=name, age=age)
