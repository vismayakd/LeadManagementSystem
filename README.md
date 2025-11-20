<!-- # Lead Management System

## Description
A Django-based Lead Management System to manage and track leads efficiently.  
Features include:
- Add, update, and delete leads
- Track lead status
- Email notifications when lead status changes

---

## Technologies Used
- Python 3.x  
- Django  
- PostgreSQL  
- Bootstrap (Frontend)  
- Celery + Redis (optional for asynchronous email tasks)

---

## Git Repository
This project is maintained in a Git repository. Make sure to clone the repository before setting it up locally:

```bash
git clone <repository_url>
cd <project_folder>



# Setup Instructions
1. Create a virtual environment
python -m venv venv
# Activate
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

2. Install dependencies
pip install -r requirements.txt

3. Create .env file

# Create a .env file in the project root and add your environment variables:

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEBUG=True



#  Credentials are not included in the repository for security reasons.
# Use your own Gmail App Password or a test SMTP service (e.g., Mailtrap).

4. Configure PostgreSQL

Update your settings.py to configure PostgreSQL. Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Make sure PostgreSQL is installed and running on your system.

5. Apply migrations
python manage.py migrate

6. Create a superuser
python manage.py createsuperuser

7. Run the development server
python manage.py runserver

8. Open the app in your browser
http://127.0.0.1:8000 -->