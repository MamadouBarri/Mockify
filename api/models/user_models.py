"""
This module contains models for all the mock
data we can retrieve from DB.

The Structure for each Model goes as follows:

    - id (implicit always incrementing primary key)
    - data (data for the specific model) can be [CharField | ]
"""

from django.db import models


class Email(models.Model):
    """
    Models for mock emails
    """
    data = models.CharField(max_length=100)


class Phone(models.Model):
    """
    Models for mock phones
    """
    data = models.CharField(max_length=15)
