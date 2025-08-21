from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Software Engineer',
#         'location': 'New York',
#         'description': 'Develop and maintain web applications.',
#         'date_posted': '2023-10-01'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'San Francisco',
#         'description': 'Analyze and interpret complex data.',
#         'date_posted': '2023-09-15'
#     },
#     {
#         'id': 3,
#         'title': 'Product Manager',
#         'location': 'Remote',
#         'description': 'Lead product development and strategy.',
#         'date_posted': '2023-08-20'
#     }
# ]



JOBS = load_jobs_from_db()

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)