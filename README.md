# Vesper: A Hybrid Mental Health Chatbot

Vesper is a conversational agent designed to support users seeking mental health information and guidance.  
It combines **rule-based retrieval, CNN-based intent classification, and generative LSTM models** for robustness and natural interaction.  
The system is served via a **Flask web app** with a simple chat-style frontend.

---

## 🚀 Features

- **Rule-Based Model**: Fast TF-IDF similarity matching for FAQs.  
- **Retrieval-Based CNN Model**: Classifies user queries into intents and retrieves accurate answers.  
- **Generative Seq2Seq Model**: Generates natural responses when other models fail.  
- **Hybrid Workflow**: Multi-step fallback for reliable and empathetic responses.  
- **Flask Frontend**: Clean chat interface styled with conversation bubbles.  

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="50" height="50"/>
</p>

---


## ⚙️ How It Works

1. **Greeting Check**  
   Matches common greetings and responds instantly.  

2. **Rule-Based Response**  
   Uses TF-IDF similarity with dataset questions.  

3. **Retrieval-Based CNN**  
   Predicts intent → retrieves answers.  

4. **Generative Seq2Seq Model**  
   Generates responses word-by-word if other methods fail.  

5. **Fallback**  
   Returns: *"Sorry, I couldn’t understand."*  

---

## 📊 Benefits of Hybrid Approach

- ✅ **Reliable**: Handles FAQs and unseen queries.  
- ✅ **Flexible**: Supports both retrieval and generation.  
- ✅ **Maintainable**: Models can be updated independently.  
- ✅ **User-Centered**: Empathetic fallback ensures naturalness.  

---

## 🔮 Next Steps

- Expand and curate dataset.  
- Add **attention / transformer-based models**.  
- Use **contextual embeddings (BERT, RoBERTa)**.  
- Enable **multi-turn conversations**.  
- Implement **feedback-based continual learning**.  

---






