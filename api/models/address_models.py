"""
This module contains models for all the mock
data we can retrieve from DB.

The Structure for each Model goes as follows:

    - id (implicit always incrementing primary key)
    - data (data for the specific model) can be [CharField | ]
"""

from django.db import models


class StreetAddress(models.Model):
    """
    Model for mock street addresses 
    """
    data = models.CharField(max_length=100)


class City(models.Model):
    """
    Model for mock cities
    """
    data = models.CharField(max_length=100)


class Zip(models.Model):
    """
    Model for mock zip codes
    """
    data = models.CharField(max_length=100)


class State(models.Model):
    """
    Model for mock state codes
    """
    data = models.CharField(max_length=10)


class CountryName(models.Model):
    """
    Model for mock countries
    """
    data = models.CharField(max_length=100)


class CountryCode(models.Model):
    """
    Model for mock countries
    """
    data = models.CharField(max_length=5)
