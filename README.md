



<p align="center">

  <h3 align="center"> :zap: Mockify :zap:</h3>
  <h4 align="center"> https://mockify-api.herokuapp.com/ (loading might take time since I am using a free version of Heroku Server) </h4>
  
<h5 align="center">By Barri</h5>
  <p align="center">
    Easy-to-use Mock REST API that let's any developer accelerate their initial development process.
    <br />
    <br />
    <a href="https://github.com/MamadouBarri/Mockify/issues">Report Bug</a>
    ·
    <a href="https://github.com/MamadouBarri/Mockify/issues">Request Feature</a>
  </p>
</p>



## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [API Usage](#usage)
  * [Local Installation](#local-installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



## About The Project


Often times, front end developers need data to prototype the UI, but the back end is not quite ready to use. Usually this issue is resolved by creating a local mock API, but the process can be tedious and repetitive. In these situations a service like *Mockify* is particularly useful!

Here's why:
* Your time should not be spent creating mock APIs, because they will eventually be replaced :clock10:
* You shouldn't be doing the same tasks over and over (DRY!)  :expressionless:
* It's easy! :white_check_mark:

![alt text](https://github.com/MamadouBarri/Mockify/blob/master/readme_assets/ui_image.PNG?raw=True)

Of course, not all types of data can be mocked with Mockify as of now, but feel free to <a href="https://github.com/MamadouBarri/Mockify/issues">request a feature </a> or even contribute to this project!


### Built With

These are the main technologies used to build and deploy this project:
* [Python 3.8.5](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [RESTFramework](https://www.django-rest-framework.org/)
* [SQLite](https://www.sqlite.org/index.html)
* [Heroku](https://www.heroku.com/)

For a more exhaustive list, feel free to check out the [requirements.txt](https://github.com/MamadouBarri/Mockify/blob/master/requirements.txt) file.

## Getting Started


### Prerequisites

* An HTTP client to make POST requests such as [Postman](https://www.postman.com/), [curl](https://curl.haxx.se/) or a library like [axios](https://github.com/axios/axios).

### Usage

Here is a simple POST request to [https://mockify-api.herokuapp.com/api/](https://mockify-api.herokuapp.com/api/) with a json schema.

```json
POST https://mockify-api.herokuapp.com/api/ HTTP/1.1
Content-Type: application/json

{
    "count": 100,
    "city": "my_city",
    "country_code": "my_country_code",
    "country_name": "my_country_name",
    "currency": "my_currency",
    "email": "my_email",
    "first_name": "my_first_name",
    "last_name": "my_last_name",
    "phone": "my_phone",
    "state": "my_state",
    "street_address": "my_street_address",
    "zip_code": "my_zip",
    "integer_number": {
        "range": "1,2",
        "name": "my_integer_number"
    },
    "float_number": {
        "range": "1,2.5",
        "name": "my_float_name"
    },
    "list_choice": {
        "range": "asdf, asdf, adf",
        "name": "my_list_choice"
    },
    "boolean_value": "my_boolean",
    "unique_identifier": "my_uid"
}
```

After this request, the server returns a json file containing a list of 100 mock objects with random data:

![alt text](https://github.com/MamadouBarri/Mockify/blob/master/readme_assets/rsz_1random_data_ex.png?raw=true)

Here are the steps to take when creating a schema object:

* Choose the number of objects to generate (max 100) and set the *count* attribute in your json
* For *city*, *country_code*, *country_name*, *currency*, *email*, *first_name*, *last_name*, *phone*, *state*, *street_address*, *zip_code*, *boolean_value* and *unique_identifier* you only need to specify the name of the attribute for a specific type of data. In our example, we wanted the server to return objects that have *my_country_code* as their attribute with *country_code* as their type. Therefore we inserted this attribute-value pair in our json:
```json
"country_code": "my_country_code"
```
* For more complex data types, we also need to specify complementary information such as a range or an enumeration of values. The *name* of the variable should be in the name *attribute* and the additional information in the *range* attribute:

```json
"list_choice": {
        "range": "asdf, asdf, adf",
        "name": "my_list_choice"
    }
```

Here is an exhaustive list of types that Mockify supports as of now:
* city : Random city from anywhere in the world. ~114k records
* country_code : Random country code (alpha-2). ~230 records
* country_name : Random country name. ~230 records
* currency : Random currency ISO4217. ~140 records
* email : Random email. ~40k records
* first_name : Random first name. ~5k records
* last_name : Random last name. ~150k records
* phone : Random phone number. ~30k records
* state : Random states throughout the world. ~1k records
* street_address : Random US street address. ~1k records
* zip_code : Random US postal code. ~1k records
* integer_number : Random integer number within the specified range.
* float_number : Random decimal point number within the specified range.
* list_choice : Random choice from the specified comma-separated list.
* boolean_value : Random boolean value
* unique_identifier : Random unique identifier.


### Local Installation

1. Clone the repo
```sh
git clone https://github.com/MamadouBarri/Mockify.git
```
2. Create a virtual environment in the cloned directory
```sh
python -m venv .
```
3. Activate virtual environment
```sh
# cmd
C:\> <venv>\Scripts\activate.bat
```
```sh
# bash/zsh
$ source <venv>/bin/activate
```
4. Install the requirements
```sh
pip install -r requirements.txt
```
5. Start the server
```sh
python manage.py runserver
```


## Contributing

Feel free to contribute to this project! I'm always open to new suggestions and ideas. Any contributions you make are **greatly appreciated**. :smile:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License


Distributed under the MIT License.

## Contact

Barri, Mamadou - mgbarri@icloud.com

Project Link: [https://github.com/MamadouBarri/Mockify](https://github.com/MamadouBarri/Mockify)



