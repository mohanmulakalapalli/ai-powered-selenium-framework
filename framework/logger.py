import os
import logging
from datetime import datetime

# Ensure log directory exists
log_dir = "selenium_ai_framework/logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
