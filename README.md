# Company API - Django REST Framework

A RESTful API built with Django and Django REST Framework for managing companies and their employees.

## Features

* **Company Management:** Create, read, update, and delete company records.
* **Employee Management:** Manage employees and link them to specific companies.
* **Custom Endpoints:** Retrieve all employees associated with a specific company.
* **Browsable API:** Utilize the built-in browsable API provided by Django REST Framework.

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (Default Database)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd DjangoRestFramework2
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Navigate to the project directory:**
   ```bash
   cd companyapi
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The API is accessible at `http://127.0.0.1:8000/api/` when running the development server locally.

### Companies (`/api/companies/`)

* `GET /api/companies/` - Get a list of all companies.
* `POST /api/companies/` - Create a new company.
* `GET /api/companies/<id>/` - Retrieve details of a specific company.
* `PUT /api/companies/<id>/` - Update a specific company.
* `DELETE /api/companies/<id>/` - Delete a company.
* `GET /api/companies/<id>/employees/` - Retrieve all employees working in a specific company.

### Employees (`/api/employees/`)

* `GET /api/employees/` - Get a list of all employees.
* `POST /api/employees/` - Add a new employee.
* `GET /api/employees/<id>/` - Retrieve details of a specific employee.
* `PUT /api/employees/<id>/` - Update an employee.
* `DELETE /api/employees/<id>/` - Delete an employee.
