



<p align="center">

  <h3 align="center"> :zap: Mockify  :zap:</h3>
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
  * [Usage](#usage)
  * [Installation](#installation)
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

Of course, not all types of data can be mocked with Mockify as of now, but feel free to <a href="https://github.com/MamadouBarri/Mockify/issues">request a feature </a> or even contribute to this project!


### Built With

These are the main technologies used to build and deploy this project:
* [Python 3.8.5](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html)
* [Heroku](https://www.heroku.com/)

For a more exhaustive list, feel free to check out the [requirements.txt](https://github.com/MamadouBarri/Mockify/blob/master/requirements.txt) file.

## Getting Started


### Prerequisites

* An HTTP client to make POST requests such as [Postman](https://www.postman.com/), [curl](https://curl.haxx.se/) or a library like [axios](https://github.com/axios/axios).

### Usage

Here is a simple POST request to [https://mockify-api.herokuapp.com/api/](https://mockify-api.herokuapp.com/api/) with a json schema.

```
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

![alt text](https://github.com/MamadouBarri/Mockify/blob/master/readme_assets/random_data_ex.PNG?raw=true)

Here are the steps to take when creating a schema object:

*
*
*

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
```sh
git clone https://github.com/your_username_/Project-Name.git
```
3. Install NPM packages
```sh
npm install
```
4. Enter your API in `config.js`
```JS
const API_KEY = 'ENTER YOUR API';
```








<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)


