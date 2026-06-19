# 🤖 Rule-Based AI Chatbot
### DecodeLabs Internship 2026 — Project 1

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Internship](https://img.shields.io/badge/DecodeLabs-2026-orange)

---

## 📌 Project Overview
A simple Rule-Based AI Chatbot built using Python. The chatbot uses a **dictionary-based knowledge base** to match user input with predefined responses. This project demonstrates the foundational concept of conversational AI before moving to ML-based NLP models.

---

## 🎯 Objective
Build an interactive chatbot that:
- Accepts user text input
- Sanitizes and processes the input
- Matches it against a predefined rule set
- Returns an appropriate response or a fallback message

---

## 🧠 How It Works

```
User Input → Sanitize (lowercase + strip) → Dictionary Lookup → Response
                                                    ↓
                                            Not Found → Fallback Message
```

---

## 📁 Project Structure

```
project1-rule-based-chatbot/
│
├── rule_based_chatbot.ipynb    # Main Jupyter Notebook (complete project)
├── chatbot.py                  # Python script version
└── README.md                   # Project documentation
```

---

## ⚙️ Key Concepts Used

| Concept | Description |
|---|---|
| Knowledge Base | Python dictionary storing question-answer pairs |
| Input Sanitization | `.lower().strip()` to normalize user input |
| Dictionary Lookup | `.get()` method with fallback default value |
| Infinite Loop | `while True` loop to keep chatbot running |
| Exit Mechanism | `exit` keyword to break the loop |

---

## 💬 Sample Conversation

```
========================================
   Welcome to DecodeBot! 🤖
   Type 'exit' to quit
========================================

You: hello
Bot: Hi there! How can I help you?

You: what is ai
Bot: AI is Artificial Intelligence — machines that think like humans!

You: what is ml
Bot: ML is Machine Learning — AI that learns from data!

You: who made you
Bot: I was built by Umar Saeed Jan at DecodeLabs!

You: thanks
Bot: You are welcome! Anything else?

You: exit
Bot: Goodbye! See you next time!
```

---

## 🚀 How to Run

**Option 1 — Jupyter Notebook:**
```bash
jupyter notebook rule_based_chatbot.ipynb
```

**Option 2 — Python Script:**
```bash
python chatbot.py
```

---

## 📚 Supported Commands

| User Input | Bot Response |
|---|---|
| hello | Hi there! How can I help you? |
| hi | Hello! What can I do for you? |
| how are you | I am doing great! Thanks for asking. |
| what is ai | AI is Artificial Intelligence — machines that think like humans! |
| what is ml | ML is Machine Learning — AI that learns from data! |
| your name | I am DecodeBot, your AI assistant! |
| who made you | I was built by Umar Saeed Jan at DecodeLabs! |
| help | I can answer questions about AI. Just ask me anything! |
| thanks | You are welcome! Anything else? |
| bye | Goodbye! Have a great day! |
| exit | Exits the chatbot |

---

## 🔮 Future Improvements
- Add more rules to expand the knowledge base
- Implement partial/fuzzy matching for better input handling
- Integrate NLP libraries (NLTK/spaCy) for intent recognition
- Move towards ML-based chatbot using transformers

---

## 👤 Author
**Umar Saeed Jan**
DecodeLabs AI Internship — Batch 2026

---
*Built with ❤️ at DecodeLabs*
