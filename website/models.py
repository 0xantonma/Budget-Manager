from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Settings(models.Model):
    settingName = models.CharField(max_length=250)
    settingValue = models.CharField(max_length=250)

class SubCategories(models.Model):
    name = models.CharField(max_length=250)
    category = ForeignKey(Categories, on_delete=models.CASCADE)
    icon = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Expenses(models.Model):
    amount = models.CharField(max_length=250)
    note = models.CharField(max_length=250)
    date = models.DateField()
    category = ForeignKey(SubCategories, on_delete=models.CASCADE)


