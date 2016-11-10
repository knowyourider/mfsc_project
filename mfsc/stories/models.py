from django.db import models

class Story(models.Model):
    slug = models.SlugField('Story short name', max_length=32, unique=True)
    second_image = models.CharField(max_length=32, blank=True, default='')
    alt_shortname = models.CharField(max_length=32, blank=True, default='')
    title = models.CharField(max_length=128)
    credit = models.CharField(max_length=64, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    related = models.CharField(max_length=128, blank=True, default='')
    actions = models.ManyToManyField('plan.Action', 
        verbose_name='Actions related to this story', blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
