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

@pyrogram.Client.on_callback_query(filters.regex(r'^progress$'))
async def ytdl_progress(bot, quu: CallbackQuery):
    d_directory = Config.DOWNLOAD_LOCATION + '/' + str(update.message.message_id)
    print(d_directory)
    smze = 0
    if not os.path.isdir(d_directory):
      sio = f'This file is not present in the directory!'
    else:
      try:
        for path, dirs, files in os.walk(d_directory):
          for f in files:
            fp = os.path.join(path, f)
            smze += os.path.getsize(fp)
            sio = humanbytes(smze)
      except:
        pass
    await quu.answer(sio)
    print(sio)
    #return sio
    
        
'''except Exception as er:
  await bot.answer(f'Error : {er}')
  print(er)
  pass  print(smze)
sio = humanbytes(smze)
await bot.answer(f"Downloaded : {sio}", True)'''

