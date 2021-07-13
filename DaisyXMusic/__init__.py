from pyrogram import Client as Bot

from DaisyXMusic.config import API_ID, API_HASH, TOKEN

app = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DaisyXMusic.modules"),
)

app.start()
run()
