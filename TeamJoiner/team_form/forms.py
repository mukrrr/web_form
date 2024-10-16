from django import forms
from django.forms import ModelForm
from .models import TeamMember

class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ('riot_ID', 'experience', 'position', 'statistics', 'discord', 'email')
        labels = {
            'riot_ID': 'Riot ID',
            'experience': 'Experience',
            'position': 'Position',
            'statistics': 'Statistics',
            'discord': 'Discord',
            'email': 'Email',
        }
        widgets = {
            'riot_ID': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%; height:40px;'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Experience', 'style': 'width:100%; height:40px;'}),
            'position': forms.Select(attrs={'class': 'form-control', 'style': 'width:100%; height:40px;'}),
            'statistics': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tracker.gg/', 'style': 'width:100%; height:40px;'}),
            'discord': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:100%; height:40px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width:100%; height:40px;'}),
        }




        def clean_email(self):
            email = self.cleaned_data.get('email')
            if '@' not in email:
                raise forms.ValidationError('Please enter a valid email address')
            return email

        def clean_statistics(self):
            statistics = self.cleaned_data.get('statistics')
            if not statistics.startswith("https://tracker.gg"):
                raise forms.ValidationError('Please enter a valid Valorant Tracker URL')
            return statistics