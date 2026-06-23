---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd sentinel

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements/base.txt

# Run migrations
python manage.py migrate

# Create an admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Domain Model

| Model | Description | Examples |
|---|---|---|
| **Target** | An asset under assessment | `example.com`, `10.10.10.0/24`, Azure Tenant |
| **Assessment** | A specific engagement | External Pentest, AD Review, Web App Assessment |
| **Finding** | A discovered vulnerability | SQLi, XSS, Weak Passwords, Anonymous SMB |
| **Evidence** | Supporting material for findings | Screenshots, Nmap output, Burp requests |

---

## Roadmap

- [x] **Milestone 1** — Authentication, dashboard, Target/Assessment/Finding CRUD, Django Admin
- [ ] **Milestone 2** — Evidence uploads, search & filtering, finding status tracking, severity metrics
- [ ] **Milestone 3** — PDF report generation, executive summaries, report templates
- [ ] **Milestone 4** — REST API, API authentication, external integrations
- [ ] **Milestone 5** — Notifications, background tasks, multi-tenant support

---

## Future Features

CVSS scoring · Asset inventory · Team collaboration · Assessment templates · Report scheduling · S3 storage · WebSocket notifications · SIEM integration · Vulnerability import/export · Activity logging

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

Sentinel is intended for **authorized** security assessment and vulnerability management activities only. Users are responsible for complying with all applicable laws, regulations, and organizational policies.
