import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7661898578").split()))

API_ID = int(os.getenv("API_ID", "29270785"))

API_HASH = os.getenv("API_HASH", "daca090679621ae8e835f62aeb9f79b2")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8129455756:AAG1t2XSLhs408M_M0BT2i3Jb3Rfob3oYRE")

OWNER_ID = int(os.getenv("OWNER_ID", "7661898578"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4762088128").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://yya242926:UG38321hqIEIzeak@cluster0.l7xru1m.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002571512933"))
