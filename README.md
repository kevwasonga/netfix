# netfix
# Django User Management System

## Overview
This Django project implements a custom user authentication system that supports both customers and companies. It allows users to register, log in, and manage their profiles. The system extends Django's built-in authentication model to use email as the primary identifier instead of a username.

## Features
- Custom user model with email authentication
- Separate user roles: Customers and Companies
- User profile management
- Django Admin integration
- Secure authentication and authorization

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- PostgreSQL or SQLite (default)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database:
   - Open `settings.py` and update the `DATABASES` section if using PostgreSQL.
   - Default is SQLite, which works without additional configuration.

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the admin credentials.

7. Run the server:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`

## Project Structure
```
project_root/
│── users/  # Custom user app
│   ├── models.py  # Custom user models
│   ├── views.py  # User authentication views
│   ├── forms.py  # User registration and login forms
│   ├── urls.py  # URL routes for users
│   ├── admin.py  # Admin panel configurations
│── templates/  # HTML templates
│── static/  # CSS, JavaScript, images
│── manage.py  # Django management script
│── requirements.txt  # Python dependencies
│── settings.py  # Django project settings
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | User registration |
| `/login/` | POST | User authentication |
| `/profile/` | GET | View user profile |
| `/logout/` | GET | Logout user |

## Troubleshooting
If you encounter migration issues:
```bash
python manage.py migrate --fake users zero
python manage.py migrate
```
If the admin panel does not recognize the custom user model, ensure `AUTH_USER_MODEL` is set in `settings.py`:
```python
AUTH_USER_MODEL = 'users.User'
```

## License
This project is licensed under the MIT License.

## Contributors
- Your Name - [GitHub](https://github.com/yourusername)

## Contact
For any issues or contributions, please open a GitHub issue or contact the maintainers.

