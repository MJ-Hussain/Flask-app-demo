# Flask-app-demo

A small Flask web application to manage job listings and collect applications. The app uses SQL Server for persistence and Bootstrap for a responsive UI.

## Features

- Home page with open job positions
- Job detail pages (responsibilities, requirements, salary)
- Per-job application form
- Stores data in SQL Server (JOBS, APPLICATIONS)
- Simple Bootstrap-based responsive UI

## Prerequisites

- Python 3.8+
- pip
- A SQL Server instance accessible from this machine
- (Optional) virtualenv or venv for an isolated environment

## Quick setup

1. Clone the repository:

   git clone <repository-url>

2. Create and activate a virtual environment (recommended):

   python -m venv .venv
   source .venv/Scripts/activate   # Windows
   source .venv/bin/activate       # macOS/Linux

3. Install dependencies:

   pip install -r requirements.txt

## Configuration

Create a `.env` file in the project root with your database credentials:

```
DB_SERVER=your_server_or_ip
DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
FLASK_ENV=development
FLASK_APP=app.py
```

(If the project loads environment variables differently, adapt accordingly.)

## Database schema (example)

Create two simple tables for jobs and applications. Example T-SQL:

```sql
-- Jobs table
CREATE TABLE JOBS (
  id INT IDENTITY(1,1) PRIMARY KEY,
  title NVARCHAR(255) NOT NULL,
  location NVARCHAR(255),
  responsibilities NVARCHAR(MAX),
  requirements NVARCHAR(MAX),
  salary NVARCHAR(100),
  posted_at DATETIME DEFAULT GETDATE()
);

-- Applications table
CREATE TABLE APPLICATIONS (
  id INT IDENTITY(1,1) PRIMARY KEY,
  job_id INT NOT NULL,
  full_name NVARCHAR(255),
  email NVARCHAR(255),
  phone NVARCHAR(100),
  resume_url NVARCHAR(1024),
  cover_letter NVARCHAR(MAX),
  applied_at DATETIME DEFAULT GETDATE(),
  FOREIGN KEY (job_id) REFERENCES JOBS(id)
);
```

## Running locally

1. Ensure `.env` is configured and the database is reachable.
2. Run the app:

   python app.py

3. Open http://localhost:5000 in your browser.

## License

MIT