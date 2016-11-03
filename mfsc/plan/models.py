from django.db import models

class CommonModel(models.Model):
    """
    Abstract class for term : short, medium etc.
    """
    TERMS = (
        (0,'undetermined'),
        (1,'short'),
        (2,'short-medium'),
        (3,'medium'),
        (4,'short-medium-long'),
        (5,'medium-long'),
        (6,'long'),
    )
    term = models.IntegerField(default=0, choices=TERMS)
    description = models.TextField()
    related = models.CharField(max_length=128, blank=True, default='')
    responsible = models.CharField(max_length=128, blank=True, default='')
    stakeholder = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.description[:20]


class Sector(models.Model):
    """docstring for Sector"""
    slug = models.SlugField('Sector short name', max_length=16, unique=True)
    title = models.CharField(max_length=32)
    body_text = models.TextField(blank=True, default='')
    
   # list of goals for given sector
    @property
    def goal_list(self):
        return Goal.objects.filter(sector_id=self.id)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Goal(CommonModel):
    """docstring for Goal"""
    sector = models.ForeignKey('plan.Sector')
    goal_num = models.IntegerField(default=0)
    body_text = models.TextField(blank=True, default='')
    
   # list of recs for given goal
    @property
    def rec_list(self):
        return Rec.objects.filter(goal_id=self.id)

   # short goal description
    @property
    def short_description(self):
        return self.description[:110] + "..."

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.description

class Rec(CommonModel):
    """docstring for Rec - Recommendation"""
    goal = models.ForeignKey('plan.Goal')
    rec_num = models.IntegerField(default=0)
    
   # list of actions for given rec
    @property
    def action_list(self):
        return Action.objects.filter(rec_id=self.id)

   # short rec description
    @property
    def short_description(self):
        return self.description[:70] + "..."

    class Meta:
        ordering = ['id']
        verbose_name = "Recommendation"

    def __str__(self):
        return self.description


class Action(CommonModel):
    """docstring for Action """
    rec = models.ForeignKey('plan.Rec')
    action_num = models.IntegerField(default=0)
    background = models.TextField(blank=True, default='')
    progress = models.TextField(blank=True, default='')
    metrics = models.TextField(blank=True, default='')
    tags = models.ManyToManyField('plan.Tag', 
        verbose_name='Tags for this action', blank=True)
    organizations = models.ManyToManyField('plan.Organization', 
        verbose_name='Organizations for this action', blank=True)
    actions = models.ManyToManyField('plan.Action', 
        verbose_name='Other actions related to this action', blank=True)

   # short goal description
    @property
    def short_description(self):
        return self.description[:50] + "..."

    class Meta:
        ordering = ['id']

    def __str__(self):
        #return self.description
        return self.rec.goal.sector.slug + " " + str(self.rec.goal.goal_num) + \
        "." + str(self.rec.rec_num) + "." + str(self.action_num)


class Tag(models.Model):
    """docstring for Tag"""
    slug = models.SlugField('Tag short name', max_length=16, unique=True)
    title = models.CharField(max_length=64)

   # list of actions with a given tag
    @property
    def action_list(self):
        return self.action_set.all()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class Organization(models.Model):
    """docstring for Organization"""
    slug = models.SlugField('Organization short name', max_length=32, unique=True)
    name = models.CharField(max_length=128)
    link_url = models.CharField(max_length=128, blank=True, default='')
    town = models.CharField(max_length=64, blank=True, default='')
    phone = models.CharField(max_length=24, blank=True, default='')

    def __str__(self):
        return self.name
        
