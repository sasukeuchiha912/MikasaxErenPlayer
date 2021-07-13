from pyrogram import Client, idle 

from DaisyXMusic.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "ErenPyro",
   api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

app.start()
idle()
