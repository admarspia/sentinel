import os
import subprocess
from pathlib import Path

PROJECT_NAME = "sentinel"

DJANGO_APPS = [
    "accounts",
    "assessments",
    "evidence",
    "reports",
]

EXTRA_DIRS = [
    "templates",
    "templates/partials",
    "templates/registration",

    "static",
    "static/css",
    "static/js",
    "static/images",

    "media",
    "media/screenshots",
    "media/reports",
    "media/uploads",

    "docs",
    "requirements",
]

EXTRA_FILES = [
    "templates/base.html",
    "templates/dashboard.html",

    "templates/partials/navbar.html",
    "templates/partials/sidebar.html",
    "templates/partials/messages.html",

    "templates/registration/login.html",
    "templates/registration/logout.html",

    "static/css/style.css",
    "static/js/app.js",

    "docs/architecture.md",
    "docs/api.md",
    "docs/deployment.md",

    "requirements/base.txt",
    "requirements/dev.txt",
    "requirements/prod.txt",

    "README.md",
]


def run(cmd):
    print("[+] " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def create_project():
    # Create project
    run([
        "django-admin",
        "startproject",
        "config",
        PROJECT_NAME
    ])

    os.chdir(PROJECT_NAME)

    # Create apps using Django
    for app in DJANGO_APPS:
        run([
            "python",
            "manage.py",
            "startapp",
            app
        ])

    # Create additional directories
    for directory in EXTRA_DIRS:
        Path(directory).mkdir(parents=True, exist_ok=True)

    # Create files
    for file in EXTRA_FILES:
        Path(file).touch(exist_ok=True)

    print("\n[+] Sentinel project scaffold created successfully.")


if __name__ == "__main__":
    create_project()
