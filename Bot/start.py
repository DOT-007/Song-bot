from pyrogram import *

@Client.on_message(filters.command("start"))
async def start(b, m):
  await m.reply("Hey, Iam Song bot use /song command.")
