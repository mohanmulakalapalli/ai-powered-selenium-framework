# from datetime import datetime
# import openai
# import os
# from config import settings

# openai.api_key = settings.OPENAI_API_KEY

# def summarize_results(text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": f"Summarize this Selenium test result professionally: {text}"}],
#             max_tokens=60
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"AI Summary Error: {str(e)}"

# def generate_report(results):
#     html = f'''
#     <!DOCTYPE html>
#     <html><head><meta charset="utf-8">
#     <title>AI Selenium Report</title>
#     <style>
#         body {{ font-family: Arial; background: #f4f4f9; padding: 30px; }}
#         .test {{ background: white; padding: 15px; margin: 10px; border-radius: 10px; }}
#     </style></head><body>
#     <h1>🤖 AI Selenium Test Report</h1>
#     <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
#     '''

#     for name, result in results:
#         summary = summarize_results(result)
#         html += f'''<div class="test">
#             <b>{name}</b><br>
#             Raw: {result}<br>
#             AI Summary: {summary}
#         </div>'''

#     html += "</body></html>"
#     # Use a relative path for the report
#     filepath = "reports/ai_selenium_report.html"
#     dir_path = os.path.dirname(filepath)
#     os.makedirs(dir_path, exist_ok=True)
#     with open(filepath, "w", encoding="utf-8") as f:
#         f.write(html)
#     return filepath



from datetime import datetime
import os
import google.generativeai as genai
from config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
for m in genai.list_models():
    print(m.name)

def summarize_results(text):
    try:
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
        response = model.generate_content(
            f"Summarize this Selenium test result professionally: {text}",
            generation_config={"max_output_tokens": 60}
        )
        return response.text.strip()
    except Exception as e:
        return f"AI Summary Error: {str(e)}"

def generate_report(results):
    html = f'''
    <!DOCTYPE html>
    <html><head><meta charset="utf-8">
    <title>AI Selenium Report</title>
    <style>
        body {{ font-family: Arial; background: #f4f4f9; padding: 30px; }}
        .test {{ background: white; padding: 15px; margin: 10px; border-radius: 10px; }}
    </style></head><body>
    <h1>🤖 AI Selenium Test Report</h1>
    <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    '''

    for name, result in results:
        summary = summarize_results(result)
        html += f'''<div class="test">
            <b>{name}</b><br>
            Raw: {result}<br>
            AI Summary: {summary}
        </div>'''

    html += "</body></html>"
    # Use a relative path for the report
    filepath = "reports/ai_selenium_report.html"
    dir_path = os.path.dirname(filepath)
    os.makedirs(dir_path, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath


