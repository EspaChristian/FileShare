# File Share

**File Share** is a Django-based web application that allows users to upload and download files with ease. It’s designed to be simple, fast, and effective for managing file transfers.

## Features

- Upload files via a web interface
- Download shared files directly
- Lightweight and easy to set up

## Screenshot

Here is the file upload page:

![Screenshot](Screenshot_2025-06-05_12_51_16.png)

![Screenshot](Screenshot_2025-06-05_12_51_27.png)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/file-share.git
   cd file-share

2. **Create and activate a virtual environment:**

   ```bash
    # On Windows
    python -m venv env
    .\env\Scripts\activate

    # On macOS/Linux
    python3 -m venv env
    source env/bin/activate


3. **Install the dependencies:**

   ```bash
    pip install -r requirements.txt

5. **Apply migrations:**

   ```bash
    python manage.py makemigrations FileShare_App
    python manage.py migrate

6. **Run the development server:**

   ```bash
    python manage.py runserver
