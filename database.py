from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(db_connection_string)

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM jobs'))

    jobs = []
    for row in result.all():
        jobs.append(row._mapping)

    print(jobs)
