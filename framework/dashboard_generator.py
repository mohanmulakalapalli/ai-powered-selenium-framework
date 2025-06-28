import json
import os
from framework.history_tracker import history_file

def generate_dashboard():
    html_path = "reports/dashboard.html"
    dir_path = os.path.dirname(html_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(history_file, "r") as f:
        history = json.load(f)

    html = """
    <!DOCTYPE html>
    <html><head><meta charset='utf-8'><title>Test History</title>
    <style>
    body { font-family: Arial; padding: 20px; background: #f4f4f9; }
    table { width: 100%; border-collapse: collapse; background: white; }
    th, td { padding: 10px; border: 1px solid #ccc; text-align: center; }
    th { background: #007BFF; color: white; }
    </style></head><body>
    <h2>📊 Selenium Test Run History</h2>
    <table><tr><th>Date</th><th>Passed</th><th>Failed</th><th>Report</th></tr>
    """

    for run in reversed(history):
        report_filename = os.path.basename(run['report'])  # Get just the filename
        html += f"<tr><td>{run['timestamp']}</td><td>{run['pass']}</td><td>{run['fail']}</td><td><a href='{report_filename}'>View</a></td></tr>"

    html += "</table></body></html>"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return html_path
