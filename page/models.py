# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class PageModel(models.Model):
    first_name = models.CharField(max_length=50, blank=True, default='')
    second_name = models.CharField(max_length=50, blank=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    date = models.DateTimeField(auto_now=True)
