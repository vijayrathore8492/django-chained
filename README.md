# django-chained

Django application, build for coding contest. Do not re-use.
  - Built on Python3
  - django 2.0

## Pre-requisities
  - python3
  - virtualenv

## Installation and setup
### Install pre-requisities
 - sudo apt-get install python3
 - sudo apt-get install python3-pip python3-dev
 - sudo pip3 install virtualenv

### Clone the repo
 - git clone https://github.com/vijayrathore8492/django-chained.git

### Run the server 
 - cd django-chained
 - virtualenv appenv
 - source appenv/bin/activate
 - pip3 install -r requirements.txt
 - python3 app/manage.py runserver [run inside virtualenv only]

## DB tables
### consumers_consumer [list of consumers]
 - "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 - "email" varchar(300) NOT NULL UNIQUE,
 - "name" varchar(300) NOT NULL

## DIR structure
```
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

## Unit Testing (Optional but highly recommended)
The unit testing file is included in the source code at app/consumers/tests.py. Follow the steps to perform unit testing. I have included basic test cases, feel free to include more.
  - Activate virtualenv `source djangoenv/bin/activate`
  - Run Tests `python3 app/manage.py test consumers`

## PS
  - This is my first app in Django. I have tried my best to keep standards but may have missed some.