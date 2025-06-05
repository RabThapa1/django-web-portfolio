# ✈️ Django Airline Booking Platform

A fictional airline booking platform built with Django to demonstrate proficiency in Python, web development best practices, and full-stack application design.

---

##  Purpose

- Real-world Django application development
- Backend development using Python
- Clean code architecture and maintainability

---

## 🚀 Features

- Flight search and booking functionality
- Admin panel to manage flights, users, and bookings
- Database seeding with sample data
- Dockerized setup for consistent development environments
- Clean, modular Django project structure

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Containerization**: Docker
- **Others**: CSV for sample data input

---

## 📁 Project Structure
- django-web-portfolio/: Root directory of the Django project.
   - **airline_booking/**: Contains the Django project configuration, settings, URLs, and WSGI/ASGI application entry points.
   - **booking/**: Core Django app that manages flight listings, bookings, and related models and views.
   - **populatedb.py**: Script used to seed the database with sample data from `randomnames.csv` for development/testing purposes.
   - **randomnames.csv**: Sample dataset used for populating mock user or flight data into the database.
   - **requirements.txt**: Lists all Python packages required for the project, used for setting up the development environment.
   - **manage.py**: Django's CLI tool used for running the server, managing migrations, and other common project commands.
   - **db.sqlite3**: SQLite database file generated locally after migrations; stores all project data during development.

---

## ⚙️ Installation

### 📦 Local Development Setup

1. **Clone the repo**:

```bash
git clone https://github.com/RabThapa1/django-web-portfolio.git
cd django-web-portfolio
```

2. **Create and Activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies
```bash
pip install -r requirements.txt
```

4. **Apply migrations
```bash
python manage.py migrate
```

5. **Create Superuser(for admin access)
```bash
python manage.py createsuperuser
```

6. **Seed the database
 ```bash
python populatedb.py
```

7.**Run the development server ( Open your browser at http://localhost:8000)
 ```bash
python populatedb.py
```

---
🐳 Docker Setup (Optional)

1. **Build Docker image
```bash
docker build -t django-airline .
```

2. **Run Container
```bash
docker run -d -p 8000:8000 django-airline
```
   

## 🙌 Acknowledgements

This project was built as part of my personal learning journey and to showcase practical Django development skills. Feedback and suggestions are always welcome!

---

© 2025 Rab Thapa. All rights reserved.

   

