from database.ia_filterdb import horridfan
from pyrogram import *


@Client.on_message(filters.command("send_channel"))
async def fuckyiurlol(n, l):
   file = await horridfan()
   for k in file:
       await n.send_cached_media(chat_id=message.from_user.id, file_id=k)
  
