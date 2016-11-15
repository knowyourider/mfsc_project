from django.db import models

class Organization(models.Model):
    """docstring for Organization"""
    slug = models.SlugField('Organization short name', max_length=32, unique=True)
    name = models.CharField(max_length=128)
    link_url = models.CharField(max_length=128, blank=True, default='')
    town = models.CharField(max_length=64, blank=True, default='')
    phone = models.CharField(max_length=24, blank=True, default='')
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ResourcePage(models.Model):
    """ 
    Pages linked from Resources menu page - wysiwyg text with lists of specific resources
    """
    slug = models.SlugField('Resource page short name', max_length=32, unique=True)
    title = models.CharField(max_length=128)
    body_text = models.TextField(blank=True, default='')
    ordinal = models.IntegerField('Order in Menu', default=99)

    class Meta:
        ordering = ['ordinal']

    def __str__(self):
        return self.slug
