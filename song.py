from HorridAPI import Songmrz
import os
from pyrogram import Client, filters
from aiohttp import web
from dotenv import load_dotenv  # Import dotenv to load environment variables
from Bot import web_server
# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
TOKEN = os.getenv("TOKEN")
API_ID = int(os.getenv("API_ID"))  # API_ID must be an integer
API_HASH = os.getenv("API_HASH")
API_KEY = os.getenv("API_KEY")

# Check if all necessary environment variables are loaded
if not all([TOKEN, API_ID, API_HASH, API_KEY]):
    raise ValueError("Missing environment variables. Please check your .env file.")


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            workers=200,
            plugins={"root": "Bot"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", 8080).start()
        print(f"{me.first_name} Now Working 😘")
        
Bot().run()
