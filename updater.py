import json
import random
import requests

# URL where SSC GK JSON is hosted
url = "https://raw.githubusercontent.com/Tajamuli279/quiz-questions/refs/heads/main/rawquestions.json"

# Step 1: Fetch questions from GitHub
response = requests.get(url)
data = response.json()

# Step 2: Get only questions list
all_questions = data.get("questions", [])

# Step 3: Randomly select 10 questions
selected_questions = random.sample(all_questions, 10) if len(all_questions) >= 10 else all_questions

# Step 4: Overwrite gk.json in the repo with 10 selected questions
with open("gk.json", "w") as f:
    json.dump({"questions": selected_questions}, f, indent=2)
