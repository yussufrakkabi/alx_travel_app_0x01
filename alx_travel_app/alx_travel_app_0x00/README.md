ALX Travel App Backend

The ALX Travel App is a Django-based backend for a travel listing platform, designed with industry best practices for scalability, maintainability, and team collaboration.
Features

    RESTful API built with Django REST Framework
    Comprehensive Documentation with Swagger UI and ReDoc
    Secure Authentication (Session-based)
    Data Validation with DRF serializers
    Versioned API (v1)
    Filtering & Search for listings and bookings
    MySQL Database for production
    Environment-based configuration
    CORS Support for cross-domain requests

Table of Contents

    ALX Travel App Backend
        Features
        Table of Contents
        Prerequisites
        Installation
        Configuration
        API Documentation
            Interactive Documentation
            Authentication
            Endpoints
                Listings
                Bookings
            Examples
                Create a Listing
                Create a Booking
                Filter Listings
        Testing
            Running Tests
            Test Coverage
        Project Structure
        License

Prerequisites

    Python 3.12+
    MySQL 8.0+
    Celery (for async tasks, future development)
    Git

Installation

Clone the repository

git clone https://github.com/your-username/alx_travel_app.git
cd alx_travel_app

Set up virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Configuration

Environment Variables Create a .env file in the project root:

# Django Settings
SECRET_KEY='your-secret-key-here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=alx_travel_db
DB_USER=alx_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=3306

# Celery (for async tasks)
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//

Database Setup

CREATE DATABASE alx_travel_db;
CREATE USER 'alx_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_user'@'localhost';
FLUSH PRIVILEGES;

Run Migrations

python manage.py migrate

API Documentation
Interactive Documentation

    Swagger UI: http://localhost:8000/api/docs/
    ReDoc: http://localhost:8000/api/redoc/

Authentication

POST /api/v1/auth/login/
Content-Type: application/json

{
   "username": "your_username",
   "password": "your_password"
}

Endpoints
Listings

    GET /api/v1/listings/ - List all listings
    POST /api/v1/listings/ - Create new listing
    GET /api/v1/listings/{id}/ - Get listing details
    PUT/PATCH /api/v1/listings/{id}/ - Update listing
    DELETE /api/v1/listings/{id}/ - Delete listing
    GET /api/v1/listings/{id}/reviews/ - Get reviews for listing

Bookings

    GET /api/v1/bookings/ - List all bookings
    POST /api/v1/bookings/ - Create new booking
    GET /api/v1/bookings/{id}/ - Get booking details
    PUT/PATCH /api/v1/bookings/{id}/ - Update booking
    DELETE /api/v1/bookings/{id}/ - Delete booking

Examples
Create a Listing

POST /api/v1/listings/
Content-Type: application/json

{
   "title": "Beachfront Villa",
   "description": "Luxury villa with ocean view",
   "price_per_night": "250.00",
   "max_guests": 6
}

Create a Booking

POST /api/v1/bookings/
Content-Type: application/json

{
   "listing": 1,
   "start_date": "2025-08-15",
   "end_date": "2025-08-22"
}

Filter Listings

GET /api/v1/listings/?max_price=300

Testing
Running Tests

# Run all tests
python manage.py test

# Run a specific test case
python manage.py test listings.tests.ModelTests

# Run a specific test method
python manage.py test listings.tests.ModelTests.test_listing_creation

Test Coverage

coverage run manage.py test
coverage report

Project Structure

alx_travel_app/
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
│
├── alx_travel_app/         # Main project package
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI config
│
└── listings/              # Listings application
    ├── migrations/        # Database migrations
    ├── __init__.py
    ├── admin.py          # Admin configuration
    ├── apps.py           # App configuration
    ├── models.py         # Database models
    ├── serializers.py    # API serializers
    ├── tests.py          # Application tests
    ├── urls.py          # App URL routes
    └── views.py         # API views
