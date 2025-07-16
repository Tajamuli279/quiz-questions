import json
import random
from datetime import datetime

def generate_gk_questions():
    sample_questions = [
        {
            "question": "Who was the first President of India?",
            "options": ["Rajendra Prasad", "S. Radhakrishnan", "Jawaharlal Nehru", "Vallabhbhai Patel"],
            "answer": "Rajendra Prasad",
            "category": "GK",
            "source": "Auto Gen",
            "date": str(datetime.today().date()),
            "shift": random.choice(["Morning", "Evening"])
        },
        {
            "question": "Which is the largest desert in India?",
            "options": ["Sahara", "Thar", "Gobi", "Karakum"],
            "answer": "Thar",
            "category": "GK",
            "source": "Auto Gen",
            "date": str(datetime.today().date()),
            "shift": random.choice(["Morning", "Evening"])
        },
        {
            "question": "What is the capital of Uttarakhand?",
            "options": ["Dehradun", "Haridwar", "Rishikesh", "Nainital"],
            "answer": "Dehradun",
            "category": "GK",
            "source": "Auto Gen",
            "date": str(datetime.today().date()),
            "shift": random.choice(["Morning", "Evening"])
        }
    ]
    return {"questions": random.sample(sample_questions * 5, 10)}  # 10 MCQs

# Step: Save to gk.json
with open("questions/gk.json", "w") as f:
    json.dump(generate_gk_questions(), f, indent=2)
