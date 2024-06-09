#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables




API_ID = "27467458" #config("API_ID", default=None, cast=int)
API_HASH = "5f8a1377516b84a34e30d6543654132a" #config("API_HASH", default=None)
BOT_TOKEN = "6966711070:AAGbrxqI6DxVpMz9j0hQf8NBHMJ2Uel0G1c" #config("BOT_TOKEN", default=None)
SESSION = "BQGjHsIARflnqur4H0LqXFLw_9ReCI2ZjTruamHZp8Y-XZqhM1ufedflT-Dc7NbpCjRCTNocclcd3upjPDRFHO_Gz78otOuelwgkx2VoXWDR8Am0IxMGWmpj0NbD7lURtupC6zM64HX8sXWkcepfvltZyKfZZaO3tWV8ml4WH1NW5I9WDsvInHsi8I1uN15uN6LXNjJLj_MvKl9IIaBjFqQWo6LaEGyA6xf4Evk0eVSuhOOIM3xvkKbsJxkUhqXCvaHNURFvVi5OGAusaAJDkJQVZfpi_HafwOtn7gOvef5vZuFClwhfl_4VWQ3__S4ZfTxvQm0HJKyokKLlQe5eg4kxiutXfQAAAAGKZUkxAA" #config("SESSION", default=None)
FORCESUB = "dscwsd" #config("FORCESUB", default=None)
AUTH = "6616860977" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
