from django.db import models

class Project(models.Model):
    slug = models.SlugField('Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=48)
    narrative = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
