import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def connect_to_database():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={os.environ.get('DB_SERVER')};"
            f"DATABASE={os.environ.get('DB_NAME')};"
            f"UID={os.environ.get('DB_USER')};"
            f"PWD={os.environ.get('DB_PASSWORD')}"
        )
        return conn
    except pyodbc.Error as e:
        print("Database connection error:", e)
        return None
    
def load_jobs_from_db():
    # This function will load job listings from the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JOBS")
        rows = cursor.fetchall()
        JOBS = []
        for row in rows:
            JOBS.append(dict(zip([column[0] for column in cursor.description], row)))
        cursor.close()
        conn.close()
        return JOBS
    return []

def load_job_from_db(job_id):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JOBS WHERE id = ?", (job_id,))
        row = cursor.fetchone()

        if row:
            return dict(zip([column[0] for column in cursor.description], row))
        
        cursor.close()
        conn.close()
    return None

def add_application_to_db(job_id, application_data):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO APPLICATIONS (id, name, email, linkedin, cover_letter, resume_url) VALUES (?, ?, ?, ?, ?, ?)",
            (job_id, application_data['name'], application_data['email'], application_data['linkedin'], application_data['cover_letter'], application_data['resume_url'])
        )
        conn.commit()
        cursor.close()
        conn.close()

