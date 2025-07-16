import json
import random
from datetime import datetime

def generate_question_set():
    sample_questions = [
        {
            "question": "Which Indian river is called the 'Sorrow of Bihar'?",
            "options": ["Ganga", "Kosi", "Son", "Gandak"],
            "answer": "Kosi",
            "category": "Indian Geography",
            "source": "Auto Gen SSC",
            "date": str(datetime.today().date()),
            "shift": random.choice(["Morning", "Evening"])
        },
        {
            "question": "Where is Chilika Lake located?",
            "options": ["West Bengal", "Odisha", "Andhra Pradesh", "Karnataka"],
            "answer": "Odisha",
            "category": "Indian Geography",
            "source": "Auto Gen SSC",
            "date": str(datetime.today().date()),
            "shift": random.choice(["Morning", "Evening"])
        }
    ]
    return {"questions": random.sample(sample_questions * 5, 10)}  # total 10

# Generate and overwrite file
with open("questions/gk.json", "w") as f:
    json.dump(generate_question_set(), f, indent=2)
