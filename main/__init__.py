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




API_ID = '27338814' #config("API_ID", default=None, cast=int)
API_HASH = '0e1b690b05167770e33901a8fc865c37' #config("API_HASH", default=None)
BOT_TOKEN = '6754037725:AAHTpClnKeVjvma8abMf9fVLRx6V073p-Hs' #config("BOT_TOKEN", default=None)
SESSION = '1AQAOMTQ5LjE1NC4xNzUuNjABu70xeBc4YCw6l0bYy1nRjalGmgjGLMZkRqBybPqEQEu1HcDOUp+dgcQKa9crhNdlwNhPoEU8fNf3diD80COQmThOGdru25zGEMG18TrVfZpr8WipcK3HhBEpfEeUflme3C01dhMe3DHRfLauEdPZHV37hA5wqk4MTXpPzB1o7QLww3sUxPzeS0gcoIhOzVeb6laPgm3JsuBAEUI0lPII2iGT4IyEQKEOdy7kz//ALUXeEctKGAcvYNiYZ5I8nB+J8Mton4fDycAVSahUl61b9hD7D51FGvvEwoUwBdWJ6WbBogQVyjG3LkfhheEX1azPumZCp6hQOM5VFqCYJPFNDG0='#config("SESSION", default=None)
FORCESUB = 'dscwsd'#config("FORCESUB", default=None)
AUTH = '7480147726'#config("AUTH", default=None)
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
