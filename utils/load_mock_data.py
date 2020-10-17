"""
This scripts helps importing new data from a random
json file into the DB. These scripts should be ran
in the interactive Django Shell.
"""
import json
import random
from string import ascii_lowercase, digits

from api.models import *

PATH_RANDOM_JSON = './mock_data/address.json'


def load_data_file(path):
    """
    Loads a json file from the speicfied path
    An equivalent Dict is returned
    """
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_random_countries(data):
    """
    Loads random country codes from ./mock_data/cities.json
    """
    country_codes = list(set([elem['country'] for elem in data]))
    cc_objects = [CountryCode(data=country_code)
                  for country_code
                  in country_codes]
    CountryCode.objects.bulk_create(cc_objects)


def load_random_cities(data):
    """
    Loads random cities names from ./mock_data/cities.json
    """
    cities = list(set([elem['name'] for elem in data]))
    city_objects = [City(data=city) for city in cities]
    City.objects.bulk_create(city_objects)


def load_country_names(data):
    """
    Loads random country names from ./mock_data/countries.json
    """
    country_names = [country['name'] for country in data]
    country_name_objects = [CountryName(data=country_name)
                            for country_name
                            in country_names]
    CountryName.objects.bulk_create(country_name_objects)


def load_currencies_codes(data):
    """
    Loads random currencies from ./mock_data/currencies.json
    """
    currency_codes = [currency_code for currency_code in data.keys()]
    currency_code_objects = [Currency(data=currency_code)
                             for currency_code
                             in currency_codes]
    Currency.objects.bulk_create(currency_code_objects)


def random_str(length):
    """
    Returns a random lowercase string with
    specified amount of characters
    """
    digits = ''.join([str(num) for num in list(range(10))])
    res = ''.join(random.choice(ascii_lowercase + digits)
                  for i in range(length))
    return res


def generate_fake_emails(amount):
    """
    Generate a specified amount of mock emails
    and saves them in DB
    {random string}@{random domain}.{random extension}
    """
    extensions = ['com', 'net', 'org', 'gov']
    domains = ["hotmail", "gmail", "aol",
               "mail", "mail", "yahoo"]
    emails = []
    for _ in range(amount):
        domain = domains[random.randint(0, len(domains)-1)]
        extension = extensions[random.randint(0, len(extensions)-1)]
        user_name = random_str(random.randint(5, 10))
        email = ''.join([user_name, '@', domain, '.', extension])
        emails.append(Email(data=email))
    Email.objects.bulk_create(emails)


def load_first_names(data):
    """
    Loads random currencies from ./mock_data/first_names.json
    """
    first_name_objects = [FirstName(data=first_name) for first_name in data]
    FirstName.objects.bulk_create(first_name_objects)


def load_last_names(data):
    """
    Loads random currencies from ./mock_data/last_names.json
    """
    last_name_objects = [LastName(data=last_name) for last_name in data]
    LastName.objects.bulk_create(last_name_objects)


def generate_random_phone():
    """
    Generates a random phone number
    """
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)


def populate_random_phone_numbers(amount):
    """
    Load random phone numbers in DB
    """
    phone_objects = [Phone(data=generate_random_phone())
                     for _ in range(amount)]
    Phone.objects.bulk_create(phone_objects)


def load_street_address(data):
    """
    Loads random addresses from ./mock_data/street_address.json
    """
    street_addresses = [address['address1'] for address in data]
    street_address_objects = [StreetAddress(data=street_address)
                              for street_address
                              in street_addresses]
    StreetAddress.objects.bulk_create(street_address_objects)


def load_zip(data):
    """
    Loads random zip codes from ./mock_data/street_address.json
    """
    zip_codes = [address['postalCode'] for address in data]
    zip_codes_objects = [Zip(data=zip_code)
                         for zip_code
                         in zip_codes]
    Zip.objects.bulk_create(zip_codes_objects)


def load_state_codes(data):
    """
    Loads random states from ./mock_data/street_address.json
    """
    state_codes = [address['state'] for address in data]
    state_codes_objects = [State(data=state_code)
                           for state_code
                           in state_codes]
    State.objects.bulk_create(state_codes_objects)
