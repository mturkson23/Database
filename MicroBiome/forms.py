from django import forms

from .models import Project


class PostForm(forms.ModelForm):
    #  tags =
    class Meta:
        model = Project
        #  fields = ("country",)
        #  fields = ("country", "platform", "disease", "study_design")
        fields = ('tags',)
        widgets = {
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput',
                "placeholder":"Search Your Keywords"})
        }
        error_css_class = 'error'
        required_css_class = 'bold'
        # https://www.webforefront.com/django/formtemplatelayout.html
        # TODO: allow empty fields
    #  def clean_rowname(self):
    #      return self.cleaned_data['country'] or None


# https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html
# https://medium.com/@viewflow/redesigning-an-autocomplete-for-django-1994fd07c0a6
