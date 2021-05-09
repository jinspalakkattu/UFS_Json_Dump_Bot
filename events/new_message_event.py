#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import json
from io import BytesIO
from pyrogram import Client
from pyrobot import LOGGER
from pyrogram.errors import (
    PeerIdInvalid,
    UserIsBlocked
)


@Client.on_message()
async def new_message_event(client, message):
    try:
        #print(message)
        with open(message) as file:
            data=json.load(file)
            
        print(len(data["sticker"]))
        #print(data_dict["sticker"][0]["file_id"])
        
        await message.reply_text(
            f"<code>{message}</code>",
            quote=True,
            disable_web_page_preview=True,
            disable_notification=True,
        )
    except (PeerIdInvalid, UserIsBlocked):
        pass
    except Exception as e:
        LOGGER.info(str(e))
        with BytesIO(str.encode(str(message))) as out_file:
            out_file.name = "json.text"
            await message.reply_document(
                document=out_file,
                caption=str(e),
                disable_notification=True,
                quote=True
            )
