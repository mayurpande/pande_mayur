# Python Web Address Book 

> Simple Flask app that allows a user to insert to a MySQL database. 

  

As requested by end user; this app should allow a user to submit a form with different fields such as firstname, lastname, address, email, phone. Mandatory fields are firstname, lastname and email. 

  

It should validate that an email. 

  

For extra precaution I checked to see if the phone number the put in numeric digits and to consider an international code. 

  

The user should also be able to insert to database via reading from XML file and it should follow all of the same validations as above. 

  

## Development setup 

Database URI:

Either you can create an environment variable on your system with the URI below and enter your password;

```
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:<yourpasswordhere>@localhost/exercise?charset=utf8mb4"
```
Or you can edit `config.py` and uncomment line #8 and enter your password into the URI and comment line #9.


OS X & Linux: 

Set up database:

```
user@pc~pande_mayur/$ mysql -u root -p
Enter password:
mysql > create database exercise;
mysql > exit
user@pc~pande_mayur/$ mysql -u root -p exercise < exercise.sql
```

Create a virtual environment within the repo and then install `requirements.txt`: 

``` 

user@pc~pande_mayur/$ python3 -m venv env 

user@pc~pande_mayur/$ source env/bin/activate 

(env) user@pc~pande_mayur/$ pip install -r requirements.txt 

(env) user@pc~pande_mayur/$ flask run 

``` 

Windows: 

Set up database:

```
C:\Program Files\MySQL\MySQL Server <your version no here>\bin>mysql.exe -u root -p
Enter password:
mysql>create database exercise;
mysql>exit
C:\Program Files\MySQL\MySQL Server <your version no here>\bin>mysql.exe -u root -p exercise < exercise.sql


```

Create a virtual environment within the repo and then install `requirements.txt`: 

``` 

C:\Users\your_user\Documents\pande_mayur\>py -m venv env 

C:\Users\your_user\Documents\pande_mayur\>env\Scripts\activate.bat 

(env) C:\Users\your_user\Documents\pande_mayur\> pip install -r requirements.txt 

(env) C:\Users\your_user\Documents\pande_mayur\> set FLASK_APP=pande_mayur

(env) C:\Users\your_user\Documents\pande_mayur\> set FLASK_ENV=development

(env) C:\Users\your_user\Documents\pande_mayur\> flask run 

``` 

Go to web page 127.0.0.1:5000. On the landing page you will see the form. You are able to add entries according to the validators.

If you go to 127.0.0.1:5000/xml it will explain in order to read from xml file you need to store the xml file in the data folder and go to 127.0.0.1:5000/xml/<yourxmlfilename.xml> and this will validate the content. You can use the existing `test.xml` in the data folder already. So for example the URL would be 127.0.0.1:5000/xml/test.xml.

There is the ability to migrate the database using flask-migrate like so;

OS X & Linux: 

Flask-Migrate

```
user@pc~pande_mayur/$ flask db init
user@pc~pande_mayur/$ flask db migrate
user@pc~pande_mayur/$ flask db upgrade

```

Windows: 

```
C:\Users\your_user\Documents\pande_mayur\>flask db init
C:\Users\your_user\Documents\pande_mayur\>flask db migrate
C:\Users\your_user\Documents\pande_mayur\>flask db upgrade

```

Please check the versions file before running `flask db upgrade`.


## Release History 

* 0.1 
* 0.2
* 0.3


