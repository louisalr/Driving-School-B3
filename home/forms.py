from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from home.models import Customer, School, Event


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
            'isManager'
        )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['first_name'].widget.attrs['required'] = 'required'
        self.fields['last_name'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-1',
                                                  'autocomplete': 'off',
                                                  'placeholder': 'Email',
                                                  'type': 'mail'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control mb-1',
                                                       'autocomplete': 'off',
                                                       'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control mb-1',
                                                      'autocomplete': 'off',
                                                      'placeholder': 'Last Name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-1',
                                                      'autocomplete': 'off',
                                                      'placeholder': 'Password',
                                                      'type': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-1',
                                                      'autocomplete': 'off',
                                                      'placeholder': 'Confirm Password',
                                                      'type': 'password'})
        self.fields['isManager'].widget.attrs.update({'class': 'form-check-input'})

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'Password',
                                                     'type': 'password'})


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = (
            'name',
            'address',
            'phone',
            'description',
            'picture_url'
        )

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['required'] = 'required'
        self.fields['address'].widget.attrs['required'] = 'required'
        self.fields['phone'].widget.attrs['required'] = 'required'
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-1',
                                                 'autocomplete': 'off',
                                                 'placeholder': 'Email',
                                                 'type': 'mail'})
        self.fields['address'].widget.attrs.update({'class': 'form-control mb-1',
                                                    'autocomplete': 'off',
                                                    'placeholder': 'First Name'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control mb-1',
                                                  'autocomplete': 'off',
                                                  'placeholder': 'Last Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-1',
                                                        'autocomplete': 'off',
                                                        'placeholder': 'Password',
                                                        'type': 'password'})
        self.fields['picture_url'].widget.attrs.update({'class': 'form-control mb-1',
                                                        'type': 'file'})


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'name',
            'date',
            'start_hour',
            'end_hour',
            'max_attendees'
        )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'Event name'})
        self.fields['date'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'type': 'date',
                                                     'placeholder': 'Event name'})
        self.fields['start_hour'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'Start hour'})
        self.fields['end_hour'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'End hour'})
        self.fields['max_attendees'].widget.attrs.update({'class': 'form-control mb-1',
                                                     'autocomplete': 'off',
                                                     'placeholder': 'Max attendees',
                                                     'type': 'number'})
