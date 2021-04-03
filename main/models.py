from django.db import models


class Phones(models.Model):
    name = models.CharField(max_length=50)
    display_dioganal = models.FloatField()
    ram = models.IntegerField()
    display_type = models.ForeignKey('Display_type', on_delete=models.RESTRICT)
    brand_id = models.ForeignKey('Brand', on_delete=models.RESTRICT)


class Display_type(models.Model):
    name = models.CharField(max_length=50)


class Brand(models.Model):
    name = models.CharField(max_length=50)
