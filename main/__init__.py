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
SESSION = '1AQAOMTQ5LjE1NC4xNzUuNjABuwyAMg099hyuTvwau2GFnLasKx2Mt6f0jU4rtbeFc+JV29uJfvU1ac5LMTvWwkIiMkjvgPwUoj0JGfbPhTUHgqDiqUZQIQxBH36WQ96MmCByW7UYvwvnW3BUWCVC4M6ReOh9yMJm+evFDAOiEqFK/CeX8W7g3Ept5McM8ypmEjtknRt73WloxemU1vPGtBQyrZo1ljotx1ql08EQD73budvAD0rvo5RlRPzZD3kI9cTz5FgURDaHNyiI1iOZKdpsZGdfjzLQEViH93e1Q9pCkkxIrRYgJXRFiDpz/8VKyFpEaIp/exskP+Y2kb6n7FZSYkMmGKES7C2f9g48D1/0VXM='#config("SESSION", default=None)
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
