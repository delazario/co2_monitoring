# CO2 Monitoring System for Industrial Facilities

Django-based web application designed to monitor and analyze CO2 emissions from industrial facilities in the Zaporizhzhia region. 

## Environment & Stack
* **Language:** Python 3.14
* **Framework:** Django 6.1.1
* **Database:** SQLite
* **Production Deployment:** uWSGI, Supervisor, Nginx

## Installation Guide

1. **Clone the repository:**
```bash
git clone https://github.com/delazario/co2_monitoring
cd co2_monitoring
```
2. **Initialize the virtual environment:**
```bash
python3 -m venv Backend/env
source Backend/env/bin/activate
```
3. **Install dependencies and apply migrations:**
```bash
cd Backend
python manage.py migrate
```
4. **Launch the local development server:**
```bash
python manage.py runserver
```
