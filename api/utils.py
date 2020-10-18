from enum import Enum
import random
import uuid
from api.models import *


class FieldName(Enum):
    """ Enum for field names"""
    CITY = 1,
    COUNTRY_CODE = 2,
    COUNTRY_NAME = 3,
    CURRENCY = 4,
    EMAIL = 5,
    FIRST_NAME = 6,
    LAST_NAME = 7,
    PHONE = 8,
    STATE = 9,
    STREET_ADDRESS = 10,
    ZIP = 11


class DynamicFieldName(Enum):
    """ Enum for fields generated dynamically """
    INTEGER_NUMBER = 1,
    FLOAT_NUMBER = 2,
    LIST_CHOICE = 3,
    BOOLEAN_VALUE = 4,
    UID = 5


def needs_nested_range(key):
    """
    Return True if the verbose field needs a nested field
    in schema
    """
    return key in {'integer_number', 'float_number', 'list_choice'}


def create_kwargs(data):
    """
    Create kwargs from request data raise Exception
    """
    my_kwargs = {}
    if 'integer_number' in data.keys():
        int_range = data['integer_number']['range'].split(sep=',')
        assert(len(int_range) == 2)
        assert(int(int_range[0]))
        assert(int(int_range[1]))
        my_kwargs['integer_range'] = data['integer_number']['range']

    if 'float_number' in data.keys():
        float_range = data['float_number']['range'].split(sep=',')
        assert(len(float_range) == 2)
        assert(float(float_range[0]))
        assert(float(float_range[1]))
        my_kwargs['float_range'] = data['float_number']['range']

    if 'list_choice' in data.keys():
        my_kwargs['choices'] = data['list_choice']['range']

    return my_kwargs


def verbose_to_enum(verbose_field_name):
    """
    Converts the verbose name of a field to 
    an Enum field
    """
    if verbose_field_name == 'city':
        return FieldName.CITY
    elif verbose_field_name == 'country_code':
        return FieldName.COUNTRY_CODE
    elif verbose_field_name == 'country_name':
        return FieldName.COUNTRY_NAME
    elif verbose_field_name == 'currency':
        return FieldName.CURRENCY
    elif verbose_field_name == 'email':
        return FieldName.EMAIL
    elif verbose_field_name == 'first_name':
        return FieldName.FIRST_NAME
    elif verbose_field_name == 'last_name':
        return FieldName.LAST_NAME
    elif verbose_field_name == 'phone':
        return FieldName.PHONE
    elif verbose_field_name == 'state':
        return FieldName.STATE
    elif verbose_field_name == 'street_address':
        return FieldName.STREET_ADDRESS
    elif verbose_field_name == 'zip_code':
        return FieldName.ZIP
    elif verbose_field_name == 'integer_number':
        return DynamicFieldName.INTEGER_NUMBER
    elif verbose_field_name == 'float_number':
        return DynamicFieldName.FLOAT_NUMBER
    elif verbose_field_name == 'list_choice':
        return DynamicFieldName.LIST_CHOICE
    elif verbose_field_name == 'boolean_value':
        return DynamicFieldName.BOOLEAN_VALUE
    elif verbose_field_name == 'unique_identifier':
        return DynamicFieldName.UID


def dynamic_random_data(d_field_name, count, **kwargs):
    """
    Query {count} records of random data from DB
    for the specified field_name
    """
    data = []
    if d_field_name == DynamicFieldName.INTEGER_NUMBER:
        lower_bound, upper_bound = kwargs['integer_range'].split(sep=',')
        lower_bound = int(lower_bound)
        upper_bound = int(upper_bound)
        data = [random.randint(lower_bound, upper_bound) for _ in range(count)]
    elif d_field_name == DynamicFieldName.FLOAT_NUMBER:
        lower_bound, upper_bound = kwargs['float_range'].split(sep=',')
        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
        data = [f'{random.random() * (upper_bound - lower_bound) + lower_bound:.2f}'
                for _ in range(count)]
    elif d_field_name == DynamicFieldName.LIST_CHOICE:
        choices = kwargs['choices']
        data = random.choices(choices.split(sep=','), k=count)
    elif d_field_name == DynamicFieldName.BOOLEAN_VALUE:
        data = [bool(random.getrandbits(1)) for _ in range(count)]
    elif d_field_name == DynamicFieldName.UID:
        data = [str(uuid.uuid1()) for _ in range(count)]
    return data


def query_random_data(field_name, count):
    """
    Query {count} records of random data from DB
    for the specified field_name
    """
    data = []
    if field_name == FieldName.CITY:
        random_offest = random.randint(0, City.objects.count() - count)
        data = [city.data for city in City.objects.all(
        )[random_offest:random_offest + count]]
    elif field_name == FieldName.COUNTRY_CODE:
        random_offest = random.randint(0, CountryCode.objects.count() - count)
        data = [country_code.data
                for country_code
                in list(CountryCode.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.COUNTRY_NAME:
        random_offest = random.randint(0, CountryName.objects.count() - count)
        data = [country_name.data
                for country_name
                in list(CountryName.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.CURRENCY:
        random_offest = random.randint(0, Currency.objects.count() - count)
        data = [currency.data
                for currency
                in list(Currency.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.EMAIL:
        random_offest = random.randint(0, Email.objects.count() - count)
        data = [email.data
                for email
                in list(Email.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.FIRST_NAME:
        random_offest = random.randint(0, FirstName.objects.count() - count)
        data = [first_name.data
                for first_name
                in list(FirstName.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.LAST_NAME:
        random_offest = random.randint(0, LastName.objects.count() - count)
        data = [last_name.data
                for last_name
                in list(LastName.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.PHONE:
        random_offest = random.randint(0, Phone.objects.count() - count)
        data = [phone_name.data
                for phone_name
                in list(Phone.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.STATE:
        random_offest = random.randint(0, State.objects.count() - count)
        data = [state.data
                for state
                in list(State.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.STREET_ADDRESS:
        random_offest = random.randint(
            0, StreetAddress.objects.count() - count)
        data = [street_address.data
                for street_address
                in list(StreetAddress.objects.all()[random_offest:random_offest + count])]
    elif field_name == FieldName.ZIP:
        random_offest = random.randint(0, Zip.objects.count() - count)
        data = [zip_code.data
                for zip_code
                in list(Zip.objects.all()[random_offest:random_offest + count])]
    return data
