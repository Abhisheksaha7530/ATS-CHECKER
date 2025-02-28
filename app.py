from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# ✅ Ensure set_page_config is the FIRST Streamlit command
st.set_page_config(page_title="ATS Checker", page_icon="📄", layout="wide")

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS for UI Enhancements
st.markdown("""
             <style>
        /* Full page light purple background */
        .stApp {
            background-color: #E6E6FA; /* Light purple */
            height: 100vh;
            width: 100vw;
            padding: 20px;
        }
        
        /* Centered bold heading */
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #301934 !important;  /* Dark text */
            text-align: center;
            margin-bottom: 10px;
            padding-top: 10px;  /* Remove extra top space */
            position: relative;
        }

        /* Thin white line under ATS Checker */
        .main-title::after {
            content: "";
            display: block;
            width: 120px; /* Longer line */
            height: 2px; /* Thinner line */
            background-color: white; /* Thin white line */
            margin: 8px auto;
        }

        /* Subtitle styles */
        .subheader {
            font-size: 20px;
            font-weight: 600;
            color: #1E1E1E !important; /* Force darker text */
            text-align: center;
        }

        /* Container with white background */
        .main-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin: auto;
            width: 80%;
        }

        /* Footer with maker name */
        .footer {
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            color: #3D3B40;
            margin-top: auto;
            padding-bottom: 10px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #E6E6FA; /* Same as page background */
            padding: 10px;
        }
    </style>

""", unsafe_allow_html=True)

# Function to interact with Gemini API
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Page Layout

st.markdown("<h1 class='main-title'>ATS Checker</h1>", unsafe_allow_html=True)

# Main Content Container
with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<h2 class='subheader'>📝 Enter Job Description</h2>", unsafe_allow_html=True)
        input_text = st.text_area("Paste the job description here:", key="input", height=150)

    with col2:
        st.markdown("<h2 class='subheader'>📤 Upload Your Resume</h2>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

        if uploaded_file:
            st.success(f"✅ Resume Uploaded: **{uploaded_file.name}**")  # Display file name

    st.markdown("</div>", unsafe_allow_html=True)

# Buttons
st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
col1, col2 = st.columns(2)

with col1:
    submit1 = st.button("📄 Analyze Resume")

with col2:
    submit3 = st.button(" Check Percentage Match")

# AI Prompt Templates
input_prompt1 = """
You are an experienced Technical HR Manager. Your task is to review the provided resume against the job description.
Please evaluate the candidate's profile, highlighting strengths and weaknesses.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with expertise in data science.
Evaluate the resume against the provided job description.
- First, provide the **percentage match**.
- Then list the **missing keywords**.
- Finally, give **improvement suggestions**.
"""

# Handling Button Clicks
with st.container():
    if submit1:
        if uploaded_file:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.markdown("<h2 class='subheader'>📄 Resume Evaluation:</h2>", unsafe_allow_html=True)
            st.success(response)
        else:
            st.warning(" Please upload a resume.")

    elif submit3:
        if uploaded_file:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.markdown("<h2 class='subheader'>🔍 Percentage Match & Feedback:</h2>", unsafe_allow_html=True)
            st.info(response)
        else:
            st.warning(" Please upload a resume.")

# Footer with Creator Name
st.markdown("<p class='footer'>Made by Abhishek Saha </p>", unsafe_allow_html=True)
