import datetime
from django.db import models

class NewsItem(models.Model):
    """
    Could be called Blog, but called News for consistency with our menu.
    """
    NEWS_MENU_ID = 7
    menu = models.ForeignKey('sitewide.Menu', default=NEWS_MENU_ID)
    slug = models.SlugField('Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    posted = models.DateField('Date posted', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    on_homepage = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title
