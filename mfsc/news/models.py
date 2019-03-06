import datetime
from django.db import models

class NewsItem(models.Model):
    """
    Could be called Blog, but called News for consistency with our menu.
    """
    STATUS_NUMS = (
        (1,'1 - on home page'),
        (2,'2 - current'),
        (3,'3 - archived'),
        (4,'4 - inactive'),
    )
    NEWS_MENU_ID = 7
    menu = models.ForeignKey('sitewide.Menu', default=NEWS_MENU_ID)
    slug = models.SlugField('Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    posted = models.DateField('Date posted', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    on_homepage = models.BooleanField(default=False)
    status_num = models.IntegerField(default=2, choices=STATUS_NUMS)
    # class ImageField(upload_to=None, height_field=None, width_field=None, 
    #   max_length=100, **options)
    news_image = models.ImageField(upload_to='news', blank=True)
    credit = models.CharField('Image credit', max_length=64, blank=True, default='')

   # short body text - selects first paragraph
    @property
    def short_body_text(self):
        display_string = self.body_text
        para_end = display_string.find("</p>") + 4
        return display_string[:para_end]

    # next, prev story, false if none
    def get_next(self):
        next_items = NewsItem.objects.filter(status_num__lt=4, posted__lt=self.posted)
        if next_items:
            return next_items.first()
        return False

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title

