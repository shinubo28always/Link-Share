# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @UNRATED_CODER</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://graph.org/file/7228e9fe7ebf6145cca11-38b598b785ee91950b.jpg"
START_PIC = "https://graph.org/file/7228e9fe7ebf6145cca11-38b598b785ee91950b.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.</b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote>» Creator: <a href=https://t.me/sitaratoons_support>Owner</a></blockquote>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote>This bot is developed by Yato (@sitaratoons_support) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</blockquote></b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/sitaratoons_support'>Admin</a>
<blockquote>
›› ◈ᴏᴡɴᴇʀ: <a href='https://t.me/sitaratoons_support'>Admin</a>
›› ◈ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ◈ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ◈ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ◈ᴅᴇᴠᴇʟᴏᴘᴇʀ: @sitaratoons_support</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Hindi_Dub_Anime_Zone'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
<blockquote>
›› ◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ 01: <a href='https://t.me/Hindi_Dub_Anime_Zone'>𝐀𝐧𝐢𝐑𝐞𝐚𝐥 - ᴀʟʟ ᴀɴɪᴍᴇs ɪɴ ʜɪɴᴅɪ ᴅᴜʙ</a>
›› ◈ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ 02: <a href='https://t.me/New_Anime_Hindi_dub_ST'>Sitaratoons - ᴀʟʟ ᴀɴɪᴍᴇs ɪɴ ʜɪɴᴅɪ ᴅᴜʙ</a>
›› ◈ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 01: <a href='https://t.me/AniReal_Chat_Group_Asia'> 𝐀𝐧𝐢𝐑𝐞𝐚𝐥 - Cʜᴀᴛ Gʀᴏᴜᴘ Asɪᴀ</a>
›› ◈ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 02: <a href='https://t.me/Anime_Chats_St'>Sitaratoons- Cʜᴀᴛ Gʀᴏᴜᴘ Asɪᴀ</a>
›› ◈ᴄʀᴇᴀᴛᴏʀ: @sitaratoons_support</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>⚠️ ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002511179462")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7273593616").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6692613520)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
