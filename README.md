<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>

<br/><br/>

# 🛡️ Sentinel

**Security Assessment Management Platform**

Sentinel is a Django-based platform that helps security professionals manage the full assessment lifecycle — from target discovery to final reporting — in one structured, centralized application.

<br/>

[Features](#features) · [Getting Started](#getting-started) · [Architecture](#architecture) · [Roadmap](#roadmap)

</div>

---

## The Problem

Security assessments generate a large volume of scattered artifacts:

| Artifact | Typically Stored In |
|---|---|
| Targets & scope | Spreadsheets |
| Findings | Text files or markdown |
| Evidence | Screenshot folders |
| Reports | Word documents |
| Notes | Notepads or Notion |

Managing all of this across disconnected tools creates gaps, inconsistencies, and lost context — especially across multiple engagements.

**Sentinel brings it all into one place.**

---

## Features

### 🔐 Authentication & Authorization
- User login and session management
- Role-based access control
- Django admin dashboard

### 🎯 Target Management
- Create and manage assessment targets
- Supports domains, IPs, internal networks, cloud environments, and custom asset types
- Track full assessment history per target

### 📋 Assessment Management
- Create and organize engagements
- Associate assessments with specific targets
- Track status and maintain timelines

### 🔍 Finding Management
- Record vulnerabilities and security issues
- Assign severity levels (Critical / High / Medium / Low / Informational)
- Document impact, remediation steps, and remediation status

### 🗂️ Evidence Management
- Upload screenshots and supporting files
- Attach evidence directly to findings
- Maintain a full audit trail

### 📄 Reporting
- Generate structured assessment reports
- Export findings lists
- Produce executive summaries and technical documentation

---

## Architecture

```
User
 └── Target
       └── Assessment
              └── Finding
                     └── Evidence
```

Each user manages **Targets** (assets being assessed). Each target has one or more **Assessments** (engagements). Each assessment contains **Findings** (vulnerabilities), and each finding is backed by **Evidence** (screenshots, files, exports).

---

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | Django |
| Frontend | Django Templates · Bootstrap · HTML · CSS · JavaScript |
| Database (Dev) | SQLite |
| Database (Prod) | PostgreSQL |
| File Storage | Django Media Storage |

---

## Project Structure

```
sentinel/
├── manage.py
│
├── config/             # Settings, URLs, WSGI/ASGI
├── accounts/           # Authentication, user management
├── assessments/        # Target and assessment logic
├── evidence/           # Evidence uploads and management
├── reports/            # Report generation
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── partials/       # Navbar, sidebar, messages
│   └── registration/   # Login, logout
│
├── static/             # CSS, JS, images
├── media/              # Runtime uploads (screenshots, reports)
├── docs/               # Project documentation
└── requirements/       # Dependency files
```

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

**1. Clone the repository**
```bash
git clone <repository-url>
cd sentinel
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements/base.txt
```

**4. Apply migrations**
```bash
python manage.py migrate
```

**5. Create an admin account**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Domain Model

| Model | Represents | Examples |
|---|---|---|
| **Target** | An asset under assessment | `example.com`, `10.10.10.0/24`, Azure Tenant, Internal Network |
| **Assessment** | A specific engagement | External Pentest, AD Review, Web App Assessment |
| **Finding** | A discovered vulnerability | SQLi, XSS, Weak Passwords, Anonymous SMB |
| **Evidence** | Supporting material | Screenshots, Nmap output, Burp Suite requests, Config exports |

---

## Roadmap

- [x] **Milestone 1** — Authentication, dashboard, Target / Assessment / Finding CRUD, Django Admin
- [ ] **Milestone 2** — Evidence uploads, search & filtering, finding status tracking, severity metrics
- [ ] **Milestone 3** — PDF report generation, executive summaries, report templates
- [ ] **Milestone 4** — REST API, API authentication, external integrations
- [ ] **Milestone 5** — Notifications, background tasks, multi-tenant support

---

## Planned Features

| Feature | Category |
|---|---|
| CVSS Scoring | Findings |
| Asset Inventory | Targets |
| Team Collaboration | Platform |
| Assessment Templates | Assessments |
| Report Scheduling | Reporting |
| S3 File Storage | Infrastructure |
| WebSocket Notifications | Platform |
| SIEM Integration | Integrations |
| Vulnerability Import / Export | Findings |
| Activity Logging | Audit |

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

Sentinel is intended for **authorized** security assessment and vulnerability management activities only. Users are responsible for complying with all applicable laws, regulations, and organizational policies. Unauthorized use is strictly prohibited.
