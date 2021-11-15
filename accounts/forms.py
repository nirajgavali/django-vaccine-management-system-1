from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ParentForm(ModelForm):
	class Meta:
		model = Parent
		fields = '__all__'
		exclude = ['user']

class DateInput(forms.DateInput):
    input_type = 'date'

# class ClientForm(ModelForm):
# 	class Meta:
# 		model = Client
# 		fields = '__all__'
# 		exclude = ['customer']
		# exclude = ['customer']
		# widgets = {
        #     'date_of_birth': DateInput(),
        # }

class ChildForm(ModelForm):
	class Meta:
		model = Child
		fields = '__all__'
		exclude = ['parent','child_age_in_days','child_age_integer','child_age_attributes']
		widgets = {
            'date_of_birth': DateInput(),
        }
		
		# exclude = ['is_shortlisted']

        # exclude = ['is_shortlisted']
        # exclude = ['is_shortlisted']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

# from datetime import datetime
# from croniter import croniter
# from django.forms import ModelForm, ValidationError
# # from .models import ScheduledReport
