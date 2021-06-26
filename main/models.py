from django.db import models
from user.models import User
from ComparePhones.helpers import upload_file_name


class Phones(models.Model):
    name = models.CharField(max_length=50)
    display_dioganal = models.ForeignKey('Display_dioganal', on_delete=models.RESTRICT)
    datetime = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    ram_type = models.ForeignKey('Ram_type', on_delete=models.RESTRICT)
    colors = models.CharField(max_length=100)
    display_type = models.ForeignKey('Display_type', on_delete=models.RESTRICT)
    brand_id = models.ForeignKey('Brand', on_delete=models.RESTRICT)
    Approximate_price = models.CharField(max_length=50)
    memory_type = models.ForeignKey('Memory_type', on_delete=models.RESTRICT)
    battery_type = models.ForeignKey('Battery_type', on_delete=models.RESTRICT)
    image = models.ImageField()


class Battery_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Ram_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Memory_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Display_dioganal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Display_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Brand(models.Model):
    parent = models.ForeignKey('Brand', on_delete=models.RESTRICT, default=None, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


class Post(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_file_name)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    @property
    def anons(self):
        if len(self.content) < 20:
            return self.content

        return self.content[:20] + "..."



