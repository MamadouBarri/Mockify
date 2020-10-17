"""
This module contains models for all the mock
data we can retrieve from DB.

The Structure for each Model goes as follows:

    - id (implicit always incrementing primary key)
    - data (data for the specific model) can be [CharField | ]
"""

from django.db import models


class FirstName(models.Model):
    """
    Model for mock first names
    """
    data = models.CharField(max_length=100)


class LastName(models.Model):
    """ 
    Model for mock last names
    """
    data = models.CharField(max_length=100)
