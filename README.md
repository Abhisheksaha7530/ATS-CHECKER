# ATS-CHECKER

ATS Checker is an AI-powered Applicant Tracking System (ATS) evaluator that analyzes resumes against job descriptions. It utilizes Google Gemini AI and PDF processing to provide a percentage match, missing keywords, and suggestions for improvement.

## Features

- **AI-Powered Resume Analysis** – Evaluates resumes against job descriptions using Google Gemini AI.
- **Percentage Match Calculation** – Provides a match percentage between the resume and job description.
- **Keyword Analysis** – Identifies missing keywords to improve ATS ranking.
- **PDF Resume Upload** – Supports PDF format for resume submission.
- **User-Friendly Interface** – Built using Streamlit for an easy-to-use experience.

---

## Installation & Setup

### Step 1: Clone the Repository
Clone the project using the following command:

```bash
git clone https://github.com/your-username/ATS-Checker.git
cd ATS-Checker
```

### Step 2: Create a Virtual Environment
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project folder and add your Google API Key:

```ini
GOOGLE_API_KEY=your_api_key_here
```

### Step 5: Run the Application
Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Technologies Used

- **Python** – Backend processing
- **Streamlit** – UI framework
- **Google Gemini AI** – AI-powered resume evaluation
- **pdf2image & PIL** – PDF processing
- **dotenv** – Environment variable management

---

## Deployment on Streamlit Cloud
To deploy your app:

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Create a new app.
4. Select your GitHub repository.
5. Set up environment variables (GOOGLE_API_KEY).
6. Click **Deploy!** 🚀

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added feature XYZ"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

---
## Contact
For any queries, reach out at [your-email@example.com](mailto:abhisheksaha112233@gmail.com).

