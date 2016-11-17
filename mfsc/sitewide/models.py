from django.db import models

class Menu(models.Model):
    """
    Each page type will use this as a foreign key
    """
    slug = models.SlugField('Menu short name', max_length=32, unique=True)
    title = models.CharField(max_length=128)
    menu_blurb = models.TextField('About this menu', blank=True, default='')

   # first paragraph of body text
    @property
    def first_para(self):
        # find first paragraph end
        i = self.menu_blurb.find('</p>')
        # return the substring from begining through that </p>
        return self.menu_blurb[0:i+4]

   # remaining paragraphs of body text
    @property
    def remaining_paras(self):
        # find first paragraph end
        i = self.menu_blurb.find('</p>')
        # return the substring from after that to end
        return self.menu_blurb[i+4:]
        
    def __str__(self):
        return self.title
