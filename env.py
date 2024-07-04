import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "20562331").strip()
API_HASH = os.getenv("API_HASH", "9e3e4148e73756a85b95fc69980b678d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7264254030:AAGthiCzHc38jg1JdrTej7hy7yg3NNsUl9Y").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://prasenchutia6:4Lyjs25XZIrztCLX@cluster0.jzgd8su.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "-1002144182000")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
