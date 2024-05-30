from django.db import models
from django.db.models import ForeignKey


# Create your models here.
# 本app,是为了学习django模型的使用

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True,default='')
    publisher = ForeignKey(Publisher,on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
