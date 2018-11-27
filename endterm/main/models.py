from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    #id = models.ForeignKey()
    FullName = models.CharField(max_length=100)
    #Date = models.DateField('date of getting')
    Gender = models.IntegerField(default=1)

    def __str__(self):
        return self.FullName

    def to_json(self):
        return {
            'Gender': self.Gender,
            'FullName': self.FullName
        }

class Category (models.Model):
    #id = models.ForeignKey
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Achievements(models.Model):
    #id = models.ForeignKey(max_length=20)
    person= models.ForeignKey(Person, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #date = models.DateTimeField('date of getting ')
    title = models.CharField(max_length=100)

    def __str__(self):
        return (self.Title, self.Person, self.category)

    def to_json(self):
        return {
            #'id':self.id,
            'person': self.person,
            'category': self.category,
            'title': self.title
}





