from django.db import models

class Menu(models.Model):
    """
    Each page type will use this as a foreign key
    """
    slug = models.SlugField('Menu short name', max_length=32, unique=True)
    title = models.CharField(max_length=128)
    menu_blurb = models.TextField('About this menu', blank=True, default='')

    def __str__(self):
        return self.title
