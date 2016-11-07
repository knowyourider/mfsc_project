from django.db import models
from plan.models import Action

class Project(models.Model):
    STATUS_NUMS = (
        (0,'0 - Draft'),
        (1,'1 - Display'),
    )
    slug = models.SlugField('Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=48)
    menu_blurb = models.TextField(blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    key_action_id = models.IntegerField(null=True, blank=True)    
    actions = models.ManyToManyField('plan.Action', 
        verbose_name='Actions related to this project', blank=True)
    ordinal = models.IntegerField('Order in Menu', default=99)
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)

   # key action
    @property
    def key_action(self):
        return Action.objects.get(pk=self.key_action_id)

    class Meta:
        ordering = ['ordinal']

    def __str__(self):
        return self.title
