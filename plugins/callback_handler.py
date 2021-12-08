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

smze = 0


async def ytdl_progress(bot, update):
    d_directory = Config.DOWNLOAD_LOCATION + '/' + str(update.message.message_id)
    try:
      for path, dirs, files in os.walk(d_directory):
        for f in files:
          fp = os.path.join(path, f)
          smze += os.path.getsize(fp)
        
      await bot.answer(f"Downloaded : {sio}", True)
    except exception as er:
      await bot.answer(f'Error : {er})
      print(er)
      pass
    print(smze)
    sio = humanbytes(smze)
    await bot.answer(f"Downloaded : {sio}", True)

