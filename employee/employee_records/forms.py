import re
from django.core.exceptions import ValidationError
from django import forms
from .models import Employee
from django.utils.translation import ugettext_lazy as _


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def clean(self):
        super(EmployeeForm, self).clean()
        name = self.cleaned_data.get('name')
        pan_number = self.cleaned_data.get('pan_number')
        email = self.cleaned_data.get('email')
        age = self.cleaned_data.get('age')
        ALPHANUMERIC = re.compile(r'^[0-9a-zA-Z]*$')
        ALPHABET = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$')
        EMAIL_REGEX = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
        if not ALPHABET.match(name):
            raise ValidationError(_("Only alphabets are allowed."))
            # self._errors['name'] = self.error_class(["Only alphabets are allowed."])
        if not ALPHANUMERIC.match(pan_number):
            raise ValidationError(_("Only alphanumeric characters are allowed"))
            # self._errors['pan_number'] = self.error_class(['Only alphanumeric characters are allowed'])
        if not EMAIL_REGEX.match(email):
            self._errors['email'] = self.error_class(["Not a Valid email address"])
        if not 100>=age>=1:
            self._errors['age'] = self.error_class(["Not a Valid age"])

        return self.cleaned_data