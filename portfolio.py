import streamlit as st

# Title and Introduction
st.title("Your Name's Portfolio")
st.write("A brief introduction about yourself and your skills")

# Experience Section
st.header("Experience")
# Add experience details here. You can use st.subheader and st.write for each experience
# For example:
st.subheader("Data Analyst Intern at ABC Company (2023)")
st.write("- Performed data analysis tasks using Python and R.")
st.write("- Developed data visualizations to communicate insights.")

# Skills Section 
st.header("Skills")
# List your skills with st.write or create a list using st.container
skills = ["Python", "Data Analysis", "Machine Learning", "Communication"]
st.write("Here are some of my key skills:")
for skill in skills:
  st.write(f"- {skill}")

# Education Section
st.header("Education")
# Add your educational details here. Similar to Experience section
st.subheader("Master's in Data Analytics, XYZ University (2024)")
st.write("- Graduated with a GPA of 3.8")

# Contact Section
st.header("Contact")
# Add your contact information here. You can use st.write or create a contact form
st.write("Feel free to reach out!")
st.write("Email: youremail@example.com")

# You can add more sections based on your needs, 
# like projects, awards, or links to your social media profiles

