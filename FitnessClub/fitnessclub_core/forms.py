from django import forms
from .models import GymMembership, GroupClass

class GymMembershipForm(forms.ModelForm):
    class Meta:
        model = GymMembership
        fields = ['name', 'description', 'cost']


class GroupClassForm(forms.ModelForm):
    class Meta:
        model = GroupClass
        fields = ['name', 'description', 'cost', 'gym']
