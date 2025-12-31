import json
import random
from pathlib import Path

BASE_DIR = Path(".")

for file in BASE_DIR.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # ✅ ONLY reshuffle if "questions" key exists
        if isinstance(data, dict) and "questions" in data:
            random.shuffle(data["questions"])

            with open(file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"✅ Reshuffled: {file.name}")
        else:
            print(f"⚠️ Skipped (no questions key): {file.name}")

    except Exception as e:
        print(f"❌ Error in {file.name}: {e}")

