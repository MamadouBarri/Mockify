"""
This module contains models for all the mock
data we can retrieve from DB.

The Structure for each Model goes as follows:

    - id (implicit always incrementing primary key)
    - data (data for the specific model) can be [CharField | ]
"""

from django.db import models


class Currency(models.Model):
    """
    Models for mock currencies
    """
    data = models.CharField(max_length=5)
