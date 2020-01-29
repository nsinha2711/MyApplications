from django.contrib.admin.views import autocomplete
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django import forms


class Employee(models.Model):
    ALPHANUMERIC_REGEX = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    # ALPHABET_REGEX = RegexValidator(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', 'Only alphabets are allowed')
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"),)
    EMAIL_REGEX = RegexValidator(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    name = models.CharField(max_length=100, blank=False, null=False,)
    # name = models.CharField(max_length=100, blank=False, null=False, validators=[ALPHABET_REGEX] )
    pan_number = models.CharField(max_length=50, unique=True, blank=False, null=False, validators=[ALPHANUMERIC_REGEX])
    age = models.IntegerField(blank=False, null=False,validators=[MaxValueValidator(100), MinValueValidator(1)])
    gender = models.CharField(max_length=20, blank=False, null=False, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=40, validators=[EMAIL_REGEX],blank=False, null=False)
    city = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        db_table = "employee"

