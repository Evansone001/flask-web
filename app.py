from flask import Flask, render_template,jsonify
from sqlalchemy import text
from database import load_jobs_from_db,load_job_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                          jobs=jobs,
                           company_name= 'Onada')


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    print(job)
    return render_template('jobdetails.html', job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
