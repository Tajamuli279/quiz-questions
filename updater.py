import json
import random
import requests

url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/ssc-gk-source.json"

response = requests.get(url)
data = response.json()

questions = data.get("questions", [])

# Pick 10 random SSC questions
output = {"questions": random.sample(questions, 10)}

# Save to gk.json
with open("gk.json", "w") as f:
    json.dump(output, f, indent=2)

