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
    PLAN_MENU_ID = 2
    menu = models.ForeignKey('sitewide.Menu', default=PLAN_MENU_ID)
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
    PLAN_MENU_ID = 2
    menu = models.ForeignKey('sitewide.Menu', default=PLAN_MENU_ID)
    slug = models.SlugField('Sector short name', max_length=16, unique=True)
    title = models.CharField(max_length=48)
    short_title = models.CharField(max_length=32, blank=True, default='')
    credit = models.CharField(max_length=64, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    
   # list of goals for given sector
    @property
    def goal_list(self):
        return Goal.objects.filter(sector_id=self.id)

   # first ssentence of body text
    @property
    def first_sentence(self):
        # find first sentence end
        i = self.body_text.find('.')
        # return the substring from begining through that .
        # strip leading <p>
        return self.body_text[3:i+1]

   # remaining body text
    @property
    def remaining_text(self):
        # find first sentence end
        i = self.body_text.find('.')
        # return the substring from after that to end
        # (doesn't need leading <p>, that's preceeds span in template)
        return self.body_text[i+1:]

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Goal(CommonModel):
    """docstring for Goal"""
    sector = models.ForeignKey('plan.Sector')
    goal_num = models.IntegerField(default=0)
    image_name = models.CharField('Story image name',  max_length=32, blank=True, default='')
    credit = models.CharField('Image credit', max_length=64, blank=True, default='')
    body_text = models.TextField(blank=True, default='')
    
   # list of recs for given goal
    @property
    def rec_list(self):
        return Rec.objects.filter(goal_id=self.id)

   # short goal description
    @property
    def short_description(self):
        cutoff = 110
        display_string = self.description
        if len(display_string) > cutoff:
            return display_string[:cutoff] + "..."
        else:
            return display_string
        
   # first paragraph of body text
    @property
    def first_para(self):
        # find first paragraph end
        i = self.body_text.find('</p>')
        # return the substring from begining through that </p>
        return self.body_text[0:i+4]

   # remaining paragraphs of body text
    @property
    def remaining_paras(self):
        # find first paragraph end
        i = self.body_text.find('</p>')
        # return the substring from after that to end
        return self.body_text[i+4:]

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
    organizations = models.ManyToManyField('resources.Organization', 
        verbose_name='Organizations related to this action', blank=True)
    actions = models.ManyToManyField('plan.Action', 
        verbose_name='Other actions related to this action', blank=True)

   # short action description for colored header bar
    @property
    def short_description(self):
        return self.description[:50] + "..."

   # medium action description for story page. Only truncate the very long ones
    @property
    def medium_description(self):
        cutoff = 355
        display_string = self.description
        if len(display_string) > cutoff:
            return display_string[:cutoff] + "..."
        else:
            return display_string

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
       
