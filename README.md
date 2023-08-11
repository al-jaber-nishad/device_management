# Device Management API

The Device Tracker Django Application is designed to help companies track corporate assets, such as phones, tablets, laptops, and other equipment, handed out to employees. It provides a user-friendly interface and API endpoints for managing company information, employees, devices, and device logs.


## Features
- User authentication with staff and regular user roles.
- CRUD operations for managing companies, employees, devices, and device logs.
- Device check-out and check-in functionality with condition tracking.
- Int

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python (3.7 or higher)
- Pipenv (recommended for virtual environment management)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/al-jaber-nishad/device_management.git
   cd document_management
   ```

2. Install project dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser for admin access:

   ```
   python manage.py createsuperuser
   ```
   or use
   ```
    username: admin
    password: password
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

### Usage

- Access the API at: `http://localhost:8000/`
- Admin Panel: `http://localhost:8000/admin/`
- API Documentation (Swagger): `http://127.0.0.1:8000/schema/swagger-ui/`

### Authentication

- Token-based authentication is used. Include the token in the request headers as: `Authorization: Token <your_token>`
Example
`Authorization: token *****`
