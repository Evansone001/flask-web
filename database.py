import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from time import sleep

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


# with engine.connect() as conn:
#   result = conn.execute(text("select * from  jobs"))
#   jobs = [dict(row) for row in result.mappings()]
#   print(jobs)
  
  # result_dicts =[]
  # for row in result.all():
  #   result_dicts.append(dict(row))
  # print(result_dicts)
  

# def test_db_connection(engine, retries=5):
#     """Test the database connection with retry logic."""
   
#     while retries > 0:
#         try:
#             # Attempt to connect to the database
#             conn = engine.connect()
#             print("Connection successful!")
#             conn.close()
#             break
#         except OperationalError as e:
#             # Handle connection failure
#             print(f"Connection failed: {e}")
#             print(f"Retrying in 5 seconds... {retries} retries left.")
#             retries -= 1
#             sleep(5)
    
#     if retries == 0:
#         raise Exception("Failed to connect to the database after several attempts")
    


