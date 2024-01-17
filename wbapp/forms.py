from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'address', 'phone', 'email', 'created']  # You can exclude 'created' if you don't want users to modify it
        widgets = {
            'created': forms.HiddenInput(),
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.exclude(id=self.instance.id).filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')
        return username
