from django.db import models

class Organization(models.Model):
    """docstring for Organization"""
    slug = models.SlugField('Organization short name', max_length=32, unique=True)
    name = models.CharField(max_length=128)
    link_url = models.CharField(max_length=128, blank=True, default='')
    town = models.CharField(max_length=64, blank=True, default='')
    phone = models.CharField(max_length=24, blank=True, default='')

    def __str__(self):
        return self.name
