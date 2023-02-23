from django.contrib.auth.forms import UserCreationForm
from django import forms
from home.models import Customer



class RegistrationForm(UserCreationForm):
    """docstring for RegistrationForm"""
    class Meta:  # define a metadata related to this class
        model = Customer
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

    is_school = forms.BooleanField(required=False, label='School Manager ?')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['first_name'].widget.attrs['required'] = 'required'
        self.fields['last_name'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-1', 
                                                    'autocomplete':'off',
                                                    'placeholder': 'Email',
                                                    'type': 'mail'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control mb-1',
                                                    'autocomplete':'off',
                                                    'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control mb-1',
                                                    'autocomplete':'off',
                                                    'placeholder': 'Last Name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-1',
                                                    'autocomplete':'off',
                                                    'placeholder': 'Password',
                                                    'type': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-1',
                                                    'autocomplete':'off',
                                                    'placeholder': 'Confirm Password',
                                                    'type': 'password'})
        self.fields['is_school'].widget.attrs.update({'class': 'form-check-input'})


