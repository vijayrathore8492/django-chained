# django-chained [Toran]

Django application, build for coding contest. Do not re-use.

  - Built on Python3
  - django 2.0

## Pre-requisities

  - **virtualenv**

# Installation and setup
Once all Pre-requisites and server setup are done, Follow below steps for setup

## Install pre-requisities
 - sudo apt-get install python3-pip python3-dev
 - sudo pip3 install virtualenv

## Clone the repo
 - git clone https://github.com/vijayrathore8492/django-chained.git

## Run the server 
 - cd django-chained
 - source authapienv/bin/activate
 - python3 manage.py runserver [it will start server on http://localhost:8000]

## DB tables
### consumers_consumer [list of consumers]
 - "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 - "email" varchar(300) NOT NULL UNIQUE,
 - "name" varchar(300) NOT NULL

## DIR structure
```
 - [djangoenv]                          #Python virtual environment
 - [app]
   - [app]
   - [consumers]                        #App Folder
     - [migrations]                     #Migrations scripts
     - [static]                         #Static files <css,js>
       - [consumers]
         - [bootstrap]                  #Bootstrap files
         - [css]                        #Stylesheets
         - [js]                         #Javascripts
     - [templates]                      #View templates
       - [consumers]
         - add.html                     #Add View template
         - index.html                   #Index View template
         - layout.html                  #Base View <All view extends this>
         - list.html                    #List View template
     - admin.py                         #Admin <not required>
     - apps.py                          #App Config
     - models.py                        #App models
     - tests.py                         #Unit test cases
     - url.py                           #URL routing
     - views.py                         #App views
   - db.sqlite.3                        #App DB
   - manage.py
   - README.md

```

## Unit Testing (Optional but highly recommonded)
Unit testing file is included in the source code at app/consumers/tests.py. Follow the steps to perform unit testing. I have included basic test cases, feel free to include more.
  - Activate virtualenv `source djangoenv/bin/activate`
  - Run Tests `python3 manage.py test consumers`

## PS
  - This is my first app in Django. I have tried my best to keep standards, but may have missed some.