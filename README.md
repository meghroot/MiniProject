MediConnect

A role-based login and registration portal for a healthcare application, built with Django. Users register as either a Doctor or a Patient and are routed to their own dashboard after login.

Features


Custom user model extending Django's built-in auth (CustomUser) with:

Role selection (doctor / patient)
Profile picture upload
Address field



Separate Doctor and Patient models linked one-to-one to the user, for future role-specific data
Registration with:

Password confirmation check
Username uniqueness check
Automatic creation of the matching Doctor/Patient record



Login with role-based redirect (doctor → doctor dashboard, patient → patient dashboard)
Logout
Media handling for uploaded profile pictures


Tech Stack


Python 3.12
Django 5.2.5
SQLite (default dev database)


Project Structure

MiniProject-main/
├── task1/                  # Django project (settings, URLs, WSGI/ASGI)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/                     # Core application
│   ├── models.py            # CustomUser, Patient, Doctor
│   ├── views.py              # register_user, login_user, dashboards, logout_user
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── login.html
│   ├── patient_dashboard.html
│   └── doctor_dashbaord.html
├── media/profiles/          # Uploaded profile pictures
├── db.sqlite3
└── manage.py

Setup


Clone the repository


bash   git clone <repo-url>
   cd MiniProject-main


Create and activate a virtual environment


bash   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies


bash   pip install django


Apply migrations


bash   python manage.py migrate


Create a superuser (optional, for Django admin)


bash   python manage.py createsuperuser


Run the development server


bash   python manage.py runserver


Visit http://127.0.0.1:8000/ in your browser.


URL Routes

PathViewDescription/login_pageLogin/registration page/register_userregister_userHandles new user registration (POST)/login_userlogin_userHandles login and role-based redirect/doctor_dashboarddoctor_dashboardDoctor's dashboard/patient_dashboardpatient_dashboardPatient's dashboard/logout_userlogout_userLogs the user out
