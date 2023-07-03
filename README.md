Service Management Django App

This is a Django web application for managing services.

Installation
Follow these steps to set up the project on your local machine.

Prerequisites
-> Python 3.x
-> XAMPP with MySQL

Step 1: Extract the zip file

Step 2: Install pip and django (You can follow https://www.djangoproject.com/download/)

Step 3: Configure the database

-> Start XAMPP and ensure that the MySQL server is running.
-> Open the phpMyAdmin interface by visiting `localhost/phpmyadmin` in your web browser.
-> Create a new database named `service_db`.

Step 4: Run database migrations

python manage.py migrate

Step 5: Start the development server

python manage.py runserver

The application should now be accessible at http://localhost:8000.
