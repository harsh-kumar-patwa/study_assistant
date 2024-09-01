import os
from config import BASE_DIR, SUBJECTS

def setup_directories():
    for subject in SUBJECTS:
        os.makedirs(os.path.join(BASE_DIR, subject), exist_ok=True)