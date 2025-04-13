from django import forms
from authuser.models import UserProfile

class InstructorCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'instructor'
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user
