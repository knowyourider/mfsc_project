from django.db import models
from plan.models import Action

class Project(models.Model):
    STATUS_NUMS = (
        (0,'0 - Draft'),
        (1,'1 - Display'),
    )
    PROJECT_MENU_ID = 3
    menu = models.ForeignKey('sitewide.Menu', default=PROJECT_MENU_ID)
    slug = models.SlugField('Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=48)
    menu_blurb = models.TextField(blank=True, default='', 
        help_text="Appears under title " \
        "on menu list. Don't add paragraph markup.")
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

class ProjectImage(models.Model):
    project = models.ForeignKey('projects.Project')
    image_num = models.IntegerField()
    image = models.ImageField(upload_to='projects', blank=True)
    credit = models.CharField('Image credit', max_length=64, blank=True, default='')
    
    class Meta:
        ordering = ['image_num']

    def __str__(self):
        return self.image.name

class ProjectPdf(models.Model):
    project = models.ForeignKey('projects.Project')
    # slug = models.SlugField('pdf short name', max_length=32, unique=True)
    pdf_num = models.IntegerField()
    pdf_file = models.FileField(upload_to='projects/pdfs', blank=True)
    title = models.CharField(max_length=48)
    
    class Meta:
        ordering = ['pdf_num']

    def __str__(self):
        return self.title

class Subproject(models.Model):
    STATUS_NUMS = (
        (0,'0 - Draft'),
        (1,'1 - Display'),
    )
    project = models.ForeignKey('projects.Project')
    slug = models.SlugField('Sub Project short name', max_length=32, unique=True)
    title = models.CharField(max_length=48)
    body_text = models.TextField(blank=True, default='')
    key_action_id = models.IntegerField(null=True, blank=True)    
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)

    def __str__(self):
        return self.title

class SubprojectImage(models.Model):
    subproject = models.ForeignKey('projects.Subproject')
    image_num = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='subprojects', blank=True)
    credit = models.CharField('Image credit', max_length=64, blank=True, default='')
    
    class Meta:
        ordering = ['image_num']

    def __str__(self):
        return self.image.name

class SubprojectPdf(models.Model):
    subproject = models.ForeignKey('projects.Subproject')
    # slug = models.SlugField('pdf short name', max_length=32, unique=True)
    pdf_num = models.IntegerField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='subprojects/pdfs', blank=True)
    title = models.CharField(max_length=48)
    
    class Meta:
        ordering = ['pdf_num']

    def __str__(self):
        return self.title
