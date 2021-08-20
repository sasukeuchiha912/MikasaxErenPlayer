import logging
from redis import StrictRedis

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from pyrogram import Client, idle 

from DaisyXMusic.config import API_ID, API_HASH, BOT_TOKEN, DATABASE_URI

app = Client(
    "ErenPyro",
   api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

app.start()

musicdb = StrictRedis.from_url(DATABASE_URI, decode_responses=True)
print("Music Database Alive:", musicdb.ping())
