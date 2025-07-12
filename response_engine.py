# Handles logic or AI replies

import pickle

# Load model and vectorizer
model = pickle.load(open("chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def get_response(user_input):
    try:
        input_vec = vectorizer.transform([user_input.lower()])
        prediction = model.predict(input_vec)[0]
        return prediction
    except:
        return "Sorry, I didn't understand that."

