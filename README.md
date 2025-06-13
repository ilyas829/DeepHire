# DeepHire
Job Search Application
A Python application using Flask and Streamlit to search for jobs based on keywords, designation, location, and experience, and generate resumes using the Grok API.
Setup
Prerequisites

Python 3.9+
Docker (optional for containerized deployment)
GitHub account
xAI Grok API key (for resume generation)

Local Setup

Clone the repository:git clone https://github.com/your-username/my-job-search-app.git
cd my-job-search-app


Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Start the Flask backend:python app.py


In a new terminal, start the Streamlit frontend:streamlit run streamlit_app.py


Access the app at http://localhost:8501.

Docker Setup

Build the Docker image:docker build -t job-search-app .


Run the container:docker run -p 5000:5000 -p 8501:8501 job-search-app


Access the app at http://localhost:8501.

Deploy to Streamlit Cloud

Push the repository to GitHub.
Sign up at https://share.streamlit.io/.
Create a new app, link your GitHub repository, and specify streamlit_app.py as the main file.
Deploy the app. Note: The Flask backend may need to be hosted separately (e.g., on Heroku).

Usage

Enter keywords, designation, location, and experience to search for jobs.
Paste your experience and a job description to generate a tailored resume.

Notes

Replace YOUR_GROK_API_KEY in resume_generator.py with your actual xAI API key.
The scraper is a placeholder; implement actual job board scraping logic.
For production, use a robust database like PostgreSQL and a WSGI server like Gunicorn.

