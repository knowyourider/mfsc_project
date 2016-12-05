from django import forms
from .models import Action, Sector, Tag
from resources.models import Organization

class ActionSearchForm(forms.Form):
    """
    Patterened after sitewide SearchForms and Lesson search in Mystic
    choices defined by the Python values_list function
    """
    q = forms.CharField(max_length=100, required=False)

    page = forms.IntegerField(required=False)

    # get sector list directly from the database
    secs = forms.MultipleChoiceField(
        choices = Sector.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    # get tag list directly from the database
    tags = forms.MultipleChoiceField(
        choices = Tag.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    # get organization list directly from the database
    orgs = forms.MultipleChoiceField(
        choices = Organization.objects.all().values_list('slug', 
            'name').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ActionSearchForm, self).__init__(*args, **kwargs)

        # self.fields['orgs'].choices = Organization.objects.filter(pk__in=[1,4,5]).values_list('slug', 
        #     'name').order_by('name')

        self.fields['orgs'].choices = Organization.objects.all().values_list('slug', 
            'name').order_by('name')

        # self.fields['orgs'].choices = Organization.objects.filter( 
            # id=Action.objects.all()[0].organizations[0].organization_id.values_list('slug', 
        #     'name').order_by('name'))

        # self.fields['orgs'].choices = Organization.objects.filter( 
        # id__lt=5).values_list('slug', 
        #     'name').order_by('name')
