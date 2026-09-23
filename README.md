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
