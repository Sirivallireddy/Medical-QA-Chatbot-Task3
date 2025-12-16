# Task 3 – Medical Question Answering Chatbot

## Overview
This project implements a **medical question answering chatbot** using a
representative subset of the **MedQuAD (Medical Question Answering Dataset)**.
The system retrieves the most relevant medical answer based on user queries
and demonstrates a retrieval-based GenAI workflow.

The application is built using **Python** and **Streamlit**, focusing on
dataset usage, information retrieval, and basic medical entity recognition.

---

## Features
- Medical question answering using MedQuAD dataset
- Retrieval-based answer selection using TF-IDF similarity
- Basic medical entity recognition (keyword-based)
- Web-based interactive interface using Streamlit
- Lightweight and easy-to-run implementation

---

## Technology Stack
- Python
- Streamlit
- Pandas
- Scikit-learn

---

## Dataset
- **Name:** MedQuAD (Sample)
- **Source:** https://github.com/abachaai/MedQuAD
- **Description:** A representative subset of medical question–answer pairs
  extracted from MPlus Health Topics.
- **Format:** CSV / Excel
- **Columns:**
  - `question`
  - `answer`

---

## Project Structure
Task3-Medical-QA-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
└── medquad.csv

yaml
Copy code

---

## How to Run the Project

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
