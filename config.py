import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HF_TOKEN = os.getenv("HF_TOKEN")
    MODEL_ID = "black-forest-labs/FLUX.2-dev"

# --- YOU ARE LIKELY MISSING THIS LINE BELOW ---
settings = Settings()