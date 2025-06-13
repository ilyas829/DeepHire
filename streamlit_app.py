import streamlit as st
import requests
import json
from resume_generator import generate_resume

st.title("Job Search Application")

# Input form
keywords = st.text_input("Keywords (e.g., Python Developer)")
designation = st.text_input("Designation (e.g., Software Engineer)")
location = st.text_input("Location (e.g., India)")
experience = st.number_input("Years of Experience", min_value=0, max_value=30, step=1)
resume_input = st.text_area("Paste your previous experience or resume details")
job_description = st.text_area("Paste job description for resume generation")

if st.button("Search Jobs"):
    payload = {
        "keywords": keywords,
        "designation": designation,
        "location": location,
        "experience": str(experience)
    }
    response = requests.post("http://localhost:5000/api/jobs", json=payload)
    if response.status_code == 200:
        jobs = response.json()
        st.write("### Job Listings")
        for job in jobs:
            st.write(f"**{job['title']}** at {job['company']}")
            st.write(f"Location: {job['location']}")
            st.write(f"Experience: {job['experience']}")
            st.write(f"Description: {job['description'][:200]}...")
            st.write(f"[Apply Here]({job['url']})")
            st.write("---")
    else:
        st.error("Error fetching jobs. Please try again.")

if st.button("Generate Resume"):
    if resume_input and job_description:
        resume = generate_resume(resume_input, job_description)
        st.write("### Generated Resume")
        st.write(resume)
    else:
        st.error("Please provide both resume details and job description.")