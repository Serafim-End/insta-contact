# coding: utf-8

from __future__ import print_function

from django import forms

from models import PageModel


class PageForm(forms.ModelForm):

    class Meta:
        model = PageModel
        fields = ('first_name', 'second_name', 'phone_number', 'email')
