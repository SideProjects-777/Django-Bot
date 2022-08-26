from django import forms
from . import models


class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = ['crew_status','site_ID', 'CX_status', 'completeness',
        'daily_progress', 'next_day_plan', 'notes', 'market', 'user']


