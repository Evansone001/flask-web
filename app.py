from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Nairobi, Kenya',
        'salary' : 'Ksh 350,000'
    },
    {
        'id' : 2,
        'title' : 'Software Developer',
        'location' : 'Mombasa, Kenya',
        'salary' : 'Ksh 250,000'
    },
    {
        'id' : 3,
        'title' : 'Backend Engineer',
        'location' : 'Remote',
        
    },
    {
        'id' : 4,
        'title' : 'Frontend Developer',
        'location' : 'Meru, Kenya',
        'salary' : 'Ksh 256,000'
    },
    
]

@app.route('/')
def hello_world():
    return render_template('home.html',
                          jobs=JOBS,
                           company_name= 'Onada')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
