from flask import Flask, jsonify, render_template
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route('/')
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)

    if not job:
        return "Job not found", 404

    return render_template('jobpage.html', job=job)


@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
