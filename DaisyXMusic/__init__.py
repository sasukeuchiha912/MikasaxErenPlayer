from pyrogram import Client, idle 

from DaisyXMusic.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "ErenPyro",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

app.start()
idle()
