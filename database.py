from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))

        jobs = []
        for row in result.all():
            jobs.append(row._mapping)

        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM jobs where id = :id'), {'id': id})
        rows = result.all()
        print(result)
        if len(rows) == 0:
            return None
        else:
            print(rows[0]._mapping)
            return rows[0]._mapping
