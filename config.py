# (©)Codexbotz
# Recife By Zaen @Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5902543558:AAFW0iERgSXxsTGD7AJSwTnNJHbopemJrPU")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10037223"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "1f2527315dbd447876973460eb2b9d50")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001691579646"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1980553307"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@saya_wiki")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://uwwhvfyp:1sZ9sTdLymtujY4irRDbOibOo6hocfex@mahmud.db.elephantsql.com/uwwhvfyp")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "chnlwiki")
GROUP = os.environ.get("GROUP", "AboutWiki")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001673468177"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001869722299"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001865354149"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1001773217767"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001855124171"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1980553307").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Halo {first}\n\nJoin dulu ege yang di bawah baru ada videonya_-</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1980553307)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
