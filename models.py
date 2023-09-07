from django.db import models
from datetime import date

# Create your models here.

class PriceList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    type = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + str(self.price) + '-' + self.type


class Person1(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name 

class Person2(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person3(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person4(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person5(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person6(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person7(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person8(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person9(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person10(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person11(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person12(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person13(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name
                                                
