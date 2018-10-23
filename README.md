# theStore

[![Build Status](https://travis-ci.org/kdaglas/theStore.svg?branch=theStore-api)](https://travis-ci.org/kdaglas/theStore)
[![Coverage Status](https://coveralls.io/repos/github/kdaglas/theStore/badge.svg?branch=theStore-api)](https://coveralls.io/github/kdaglas/theStore?branch=theStore-api)

Store manager is a web application that helps store owners manage sales and product inventory records. This application helps the store owner avoid selling products that have run out of stock. This app is hosted at:
- [www.theStore.com](https://kdaglas.github.io/theStore/UI/index.html)

## theStore-api

The api allows the user(store attendant or store owner) to post and get data from the app through API end points that are creating a connection of the client with the database(datastructures). API is being hosted by heroku at: 
- [www.theStore-api.com](https://douglas-thestore.herokuapp.com)

### Prerequisites

- Use a web browser preferrably Chrome.
- You need to have Python3 installed on your computer. To install it go to [www.python.org](https://www.python.org/). Note: Python needs to be installed globally (not in the virtual environment)

### Features

- User(store owner) can add a product
- User(store owner and store attendant) can view all added products
- User(store owner and store attendant) can view a specific added product
- User(store attendant) can create a sale record
- User(store owner) can view all created sale records
- User(store owner and store attendant) can view a single sale record

### Getting Started

Clone the project to your computer either by downloading the zip or using git. If you are downloading it then choose theStore-api branch and download that. To use git, run the code below:
```
    git clone https://github.com/kdaglas/theStore.git
```
If you have cloned the project, then change the branch by checking out to theStore-api branch. use this code:
```
    git checkout theStore-api
```
Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements necessary for the app to function. Below are the steps to take:
```
    $ cd theStore-api
    $ virtualenv envn <or any name of your choice>

    <!-- for ubuntu use this command-->
    $ source envn/bin/activate

    <!-- for windows use this command-->
    $ envn\Scripts\activate

    $ pip install -r requirements.txt
```
When this is done then run the application by typing this command
```
    $ python run.py
```
You can use Postman to checkout the functionality of the api endpoints, you can download here:
- [www.getpostman.com/apps](https://www.getpostman.com/apps) - Postman: An API testing tool for developers


### Tests

To run tests, make sure that pytest or nose is installed. you can run that command to install them
```
    $ pip install -r requirements.txt
```
Then run these commands to begin testing the API
```
    $ nosetests

    <!-- or -->
    $ pytest
```

### Endpoints covered.

 HTTP Method | End point | Action | Access
-------|-------|-------|-------
 POST | /api/v1/products | Create a product | only the store owner/admin
 GET | /api/v1/products | Fetch all products | both
 GET | /api/v1/products/<productId> | Fetch a single product record | both
 POST | /api/v1/sales | Create a sale order | only the store attendant
 GET | /api/v1/sales | Fetch all sale records | only the store owner/admin
 GET | /api/v1/sales/<saleId> | Fetch a single sale record | only the store owner/admin and the creator (store attendant)

### Built With

- HTML5 and CSS3
- [Python](https://www.python.org/)

### Authors

Douglas Kato
