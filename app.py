from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load all model files at app startup
qa_df = pd.read_csv('model_files/chatbot_qa.csv')
vectorizer = joblib.load('model_files/tfidf_vectorizer.joblib')
pattern_vectors = joblib.load('model_files/pattern_vectors.joblib')

def preprocess_text(text):
    # Lowercase, basic cleaning (match train-time)
    import re
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_rule_based_response(user_input, threshold=0.3):
    user_input_processed = preprocess_text(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarities = cosine_similarity(user_vec, pattern_vectors).flatten()
    best_index = np.argmax(similarities)
    best_score = similarities[best_index]
    if best_score >= threshold:
        return qa_df.iloc[best_index]['Answers']
    else:
        return "Sorry, I couldn't understand or find a suitable answer."

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    response = get_rule_based_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
