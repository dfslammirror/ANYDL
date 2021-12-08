import asyncio
import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from helper_funcs.display_progress import humanbytes
#from plugins.youtube_dl_button import d_directory

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

'''d_directory = Config.DOWNLOAD_LOCATION + '/' + str(update.message_id)
smze = 0


ads = d_directory()
@Client.on_callback_query(filters.regex(r'^progress$'))
async def ytdl_progress(bot, cb: CallbackQuery):
    for path, dirs, files in os.walk(d_directory):
        for f in files:
          fp = os.path.join(path, f)
          smze += os.path.getsize(fp)
    
    print(smze)
    sio = humanbytes(smze)
    await cb.answer(f"Downloaded : {sio}", True)
'''
