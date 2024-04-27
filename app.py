from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Tokyo, Japan',
        'salary': '¥500,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Osaka, Japan',
        'salary': '¥400,000',
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'New York, USA',
        'salary': '$120,000',
    },
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
