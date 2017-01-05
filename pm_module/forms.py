from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['title','client_name','project_owner','actual_start_date','actual_end_date','start_date','end_date',
                  'description','status']

        # fields = ['title']