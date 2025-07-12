import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("training_data.csv")

# Split features and labels
X = df["question"]
y = df["answer"]

# Vectorize input questions
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train ML model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")
