#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
'''end_one = datetime.now()
        command_to_exec = [
        "curl", "https://api.gofile.io/getServer"
        ]
        try:
            logger.info(command_to_exec)
            t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            logger.info("Status : FAIL", exc.returncode, exc.output)
            server= t_response.split('"')[6]
            url = f"https://{server}.gofile.io/uploadFile"
'''

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from datetime import datetime
import os
import requests
import subprocess
import time
import re

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.display_progress import progress_for_pyrogram, humanbytes
from helper_funcs.ran_text import ran

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@pyrogram.Client.on_message(pyrogram.filters.command(["getlink4"]))
async def get_link(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    logger.info(update.from_user)
    if update.reply_to_message is not None:
        reply_message = update.reply_to_message
        download_location = Config.DOWNLOAD_LOCATION + "/" + ran + "/"
        start = datetime.now()
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_FILE,
            reply_to_message_id=update.message_id
        )
        c_time = time.time()
        after_download_file_name = await bot.download_media(
            message=reply_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_FILE,
                a,
                c_time
            )
        )
  
        download_extension = after_download_file_name.rsplit(".", 1)[-1]
        download_file_name_1 = after_download_file_name.rsplit("/",1)[-1]
        download_file_name = download_file_name_1.rsplit(".",1)[0]
        url= 'https://file.io'
        s0ze = os.path.getsize(after_download_file_name)
        if after_download_file_name is None:
            await bot.edit_message_text(
                text=Translation.FILE_NOT_FOUND,
                chat_id=update.chat.id,
                message_id=a.message_id
        )
        else:
            end_one = datetime.now()
            command_to_exec = [
            "curl",
            "-F", f"file=@\"{after_download_file_name}\"", url
        ]
        await bot.edit_message_text(
            text=f"Uploading... \n\n TO File.io",
            chat_id=update.chat.id,
            message_id=a.message_id
        )
        try:
            logger.info(command_to_exec)
            t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            logger.info("Status : FAIL", exc.returncode, exc.output)
            await bot.edit_message_text(
                chat_id=update.chat.id,
                text=exc.output.decode("UTF-8"),
                message_id=up.message_id
            )
            return False
        else:
            logger.info(t_response)
            t_response_array = t_response.decode("UTF-8").split("\n")[-1].strip()
            #t_response_ray = re.findall("(?P<url>https?://[^\s]+)", t_response_array)
            t_response_ray = t_response_array.rsplit('"')
        await bot.edit_message_text(
            chat_id=update.chat.id,
            text= Translation.AFTER_GET_DL_LINK.format(download_file_name_1, s0ze, t_response_ray[9]),
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Download Link", url=t_response_ray[9])],
    ]),
            message_id=a.message_id,
            disable_web_page_preview=True
        )
        try:
            os.remove(after_download_file_name)
        except:
            pass
    else:
        await bot.edit_message_text(
            chat_id=update.chat.id,
            text=Translation.REPLY_TO_DOC_GET_LINK,
            message_id=a.message_id
        )
