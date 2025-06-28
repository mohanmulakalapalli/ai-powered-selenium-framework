import json
import os
from datetime import datetime

history_file = "selenium_ai_framework/results/history.json"

def append_history(pass_count, fail_count, report_path):
    os.makedirs(os.path.dirname(history_file), exist_ok=True)
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pass": pass_count,
        "fail": fail_count,
        "report": report_path.replace("selenium_ai_framework/", "")
    }

    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    with open(history_file, "w") as f:
        json.dump(data, f, indent=2)
