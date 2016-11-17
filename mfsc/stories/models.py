from django.db import models

class Story(models.Model):
    STORY_MENU_ID = 4
    menu = models.ForeignKey('sitewide.Menu', default=STORY_MENU_ID)
    slug = models.SlugField('Story short name', max_length=32, unique=True)
    second_image = models.CharField(max_length=32, blank=True, default='')
    alt_shortname = models.CharField(max_length=32, blank=True, default='')
    title = models.CharField(max_length=128)
    credit = models.CharField(max_length=64, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    related = models.CharField(max_length=128, blank=True, default='')
    ordinal = models.IntegerField('Order in Menu', default=99)
    actions = models.ManyToManyField('plan.Action', 
        verbose_name='Actions related to this story', blank=True)

    class Meta:
        ordering = ['ordinal', 'id']

    def __str__(self):
        return self.title
