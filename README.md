# Employee Management System - Django

A web-based Employee Management System built using Django. This project demonstrates a complete CRUD (Create, Read, Update, Delete) functionality with a user-friendly interface for managing employee data. 

## Features

- Add, view, update, and delete employee records
- Organized project structure following Django best practices
- Responsive templates and clean UI
- Easy to extend and customize for other management purposes

## Tech Stack

- **Backend:** Django  
- **Database:** SQLite (default Django DB, can be switched to PostgreSQL/MySQL)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Version Control:** Git & GitHub  


## How to Use this Project?
***
- Install Python to your System.
- Run Following command to your terminal.
    ```python
    pip install django
    ```
- Install Pipenv for Virtual Environment, run the command...
    ```python
    pip install pipenv
    ```
- Clone the repository to your local system.
- Enter in Virtual Environment by running following command in Current Working Directory.
    ```python
    pipenv shell
    ```
- Setup PostgreSQL Database and update database name and password in settings.py file in employeemanagement.
- Make the Migrations, run the command
    ```python
    python manage.py makemigrations
    ```
- Migrate the App, run the command
    ```python
    python manage.py migrate
    ```
- Finally Run the App, run the command.
    ```python
    python manage.py runserver
    ```


## Thank You
