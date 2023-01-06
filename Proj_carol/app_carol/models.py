from django.db import models
from datetime import datetime

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    added_at=models.DateTimeField(default=datetime.now, null=True,blank=True)
    
    
    class Meta:
        db_table="new_recruits"

class under_person(models.Model):
    title = models.CharField(max_length=100)
    particular  = models.CharField(max_length=200)
    lf = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=200)
    total = models.FloatField(max_length=200)
    added_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        db_table ="VARIETY"

