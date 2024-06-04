import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from time import sleep
import logging
from sqlalchemy.exc import SQLAlchemyError

# Database connection details
if 'DATABASE_URL' in os.environ:
    database_url = os.environ['DATABASE_URL']
else:
    # Handle the case where the environment variable is missing
    raise ValueError("Error: 'DATABASE_URL' environment variable not found.")

SSL_CA = "/etc/ssl/singlestore_bundle.pem"

# Create the SQLAlchemy engine
try:
    engine = create_engine(database_url,
                           connect_args={
                               'ssl': {
                                   'ssl_ca': SSL_CA
                               }
                           })
except OperationalError as e:
    # Handle connection failure
    print(f"Connection failed: {e}")
    # Provide instructions on how to set the environment variable
    print("Please set the 'DATABASE_URL' environment variable with the correct database connection string.")
    raise SystemExit(1)

# Helper function to connect to the database
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [dict(row) for row in result.mappings()]
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        rows = [dict(row) for row in result.mappings()]  # Fetch all rows as a list of dictionaries
        if len(rows) == 0:
            return None
        else:
            return rows[0]  # Return the first (and only) job dictionary

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO job_applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    params = {
          "job_id": int(job_id),
          "full_name": data['full_name'],
          "email": data['email'],
          "linkedin_url": data['linkedin_url'],
          "education": data['education'],
          "work_experience": data['work_experience'],
          "resume_url": data['resume_url'],
      }

    conn.execute(query, params)

#     try:
#         with engine.connect() as conn:
#             query = text("""
#                 INSERT INTO applications (
#                     job_id, full_name, email, linkedin_url, education, work_experience, resume_url
#                 ) VALUES (
#                     :job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url
#                 )
#             """)
#             conn.execute(query, {
#                 'job_id': job_id,  # Ensure job_id is an integer
#                 'full_name': data['full_name'],
#                 'email': data['email'],
#                 'linkedin_url': data.get('linkedin_url', ''),
#                 'education': data.get('education', ''),
#                 'work_experience': data.get('work_experience', ''),
#                 'resume_url': data.get('resume_url', '')
#             })
#             logging.info(f"Application for job_id {job_id} added successfully.")
#     except SQLAlchemyError as e:
#         logging.error(f"Error adding application for job_id {job_id}: {e}")
#         raise


# def load_job_from_db(id):
#   # with engine.connect() as conn:
#   #   result = conn.execute(text("SELECT * FROM jobs WHERE id= :val"), #small error here made me question  my life !hahaha
#   with engine.connect() as conn:
#       result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
#       rows =  [dict(row) for row in result.mappings()]  # Fetch all rows as a list
#       if len(rows) == 0:
#           return None
#       else:
#           return rows # Iterate over rows and convert each to a dictionary



   


