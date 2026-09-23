# Attachlink — Student Attachment Management System

A Django web application that connects **students** with **companies** for attachment (internship) placements. Students can browse and apply for attachment positions, companies can post openings and review applicants, and both parties can manage tasks, reports, and feedback through a unified dashboard.

---

## 📖 Overview

Attachlink streamlines the attachment process by providing:

- A **student portal** — profile setup, browse positions, apply, submit reports, view feedback
- A **company portal** — company profile, post attachment positions, review applicants, assign tasks, give feedback
- An **admin dashboard** — verify students and companies, oversee all activity
- An integrated **reports & tasks system** — track progress throughout the attachment period

---

## ✨ Features

### Student side
- Registration and authentication
- Profile setup and editing
- Browse available attachment positions
- Apply for positions
- View application status
- Receive and complete assigned tasks
- Submit progress reports
- View company feedback

### Company side
- Company registration and profile setup
- Post new attachment positions
- Browse applicants for each position
- Review student profiles
- Assign tasks to attached students
- Provide feedback on submitted reports

### Admin side
- Custom admin dashboard
- Verify student and company accounts
- Monitor all applications, attachments, and reports

### System
- Django authentication (login, logout, password reset)
- Environment-based configuration (secrets via `.env`)
- SQLite for development
- Clean app separation (`accounts`, `students`, `companies`, `attachments`, `reports`, `core`)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Language | Python 3.10+ |
| Database | SQLite (development) |
| Templating | Django Templates + HTML |
| Config | `python-dotenv` |
| Images | Pillow |

---

## 📁 Project Structure

```
attachlink/
├── accounts/          # User auth, registration, login, dashboards
├── attachments/       # Attachment positions, applications
├── companies/         # Company profiles and dashboard
├── students/          # Student profiles and dashboard
├── reports/           # Tasks, reports, feedback
├── core/              # Project settings, URLs, WSGI/ASGI
├── templates/         # HTML templates (organized by app)
├── manage.py
├── requirements.txt
├── attachlink-data.json    # Sample database fixture
└── .env               # Local secrets (not committed)
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Youngosano19/attachlink.git
cd attachlink
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Generate a secure secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Load the sample database (optional)

```bash
python manage.py loaddata attachlink-data.json
```

### 7. Create a superuser (if not using the sample data)

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

### 9. Open in your browser

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## 🔐 Environment & Security

This project uses environment variables to keep secrets out of version control.

- `.env` stores `SECRET_KEY` and `DEBUG`
- `.env` is **excluded** from Git via `.gitignore`
- `db.sqlite3`, `media/`, `__pycache__/`, and `venv/` are also excluded

**Never commit your `.env` file or real credentials.**

---

## 👤 Author

**Peter Young Osano**
- GitHub: [@Youngosano19](https://github.com/Youngosano19)

---

## 📄 License

This project was built for academic purposes. Contact the author for reuse or collaboration.
