import streamlit as st
from web import generate_cold_email

st.title("📧 GEN AI Cold Email Generator ")

name = st.text_input("Your Name")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")
job_link = st.text_input("Job Post URL")

uploaded_file = st.file_uploader(
    "Upload CSV (skills & projects)",
    type=["csv"]
)

st.caption("CSV columns: skill, project")

if st.button("Generate Email"):
    if not all([name, linkedin, github, job_link, uploaded_file]):
        st.warning("Please fill all fields")
    else:
        with st.spinner("Generating cold email..."):
            result = generate_cold_email(
                job_link,
                name,
                linkedin,
                github,
                uploaded_file
            )

        st.subheader("📌 Subject Lines")
        for s in result["subject_lines"]:
            st.write("•", s)

        st.subheader("✉️ Email Body")
        st.text_area(
            "Copy Email",
            result["email_body"],
            height=300
        )
