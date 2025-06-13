from flask import Flask, jsonify, request
from scraper import scrape_jobs
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200))
    location = db.Column(db.String(100))
    experience = db.Column(db.String(50))
    description = db.Column(db.Text)
    url = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'experience': self.experience,
            'description': self.description,
            'url': self.url
        }

@app.route('/api/jobs', methods=['POST'])
def search_jobs():
    data = request.get_json()
    keywords = data.get('keywords')
    designation = data.get('designation')
    location = data.get('location')
    experience = data.get('experience')

    # Scrape jobs
    jobs = scrape_jobs(keywords, designation, location, experience)
    
    # Store jobs in database
    for job in jobs:
        job_entry = Job(
            title=job['title'],
            company=job.get('company', ''),
            location=job.get('location', ''),
            experience=job.get('experience', ''),
            description=job.get('description', ''),
            url=job.get('url', '')
        )
        db.session.add(job_entry)
    db.session.commit()

    return jsonify([job.to_dict() for job in Job.query.all()])

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)