from django import forms
from django.contrib.auth.hashers import make_password

from daiyn_zhauaptar.users.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
