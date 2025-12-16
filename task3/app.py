import streamlit as st
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- SAFE CSV LOADER ----------
rows = []
with open("data/medquad.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            question = row[0]
            answer = ",".join(row[1:])
            rows.append([question, answer])

data = pd.DataFrame(rows, columns=["question", "answer"])
# ------------------------------------

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(data["question"])

medical_entities = [
    "a1c", "diabetes", "abortion", "abscess", "acne",
    "tumor", "infection", "pain", "treatment", "symptoms"
]

st.title("Medical Q&A Chatbot (Task 3)")

user_query = st.text_input("Ask a medical question")

if st.button("Get Answer"):
    if user_query.strip():
        query_vector = vectorizer.transform([user_query])
        scores = cosine_similarity(query_vector, question_vectors)
        idx = scores.argmax()

        st.subheader("Answer")
        st.write(data.iloc[idx]["answer"])

        st.subheader("Detected Medical Entities")
        found = [e for e in medical_entities if e in user_query.lower()]
        st.write(", ".join(found) if found else "No entities detected.")
