# Copyright (C) 2020 KeselekPermen69
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.nhentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1) 
    chat = "@nHentaiBot"
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=424466890))
              msg = await bot.send_message(chat, link)
              response = await response
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError: 
              await event.reply("```Please unblock @nHentaiBot and try again```")
              return
          if response.text.startswith("**Sorry I couldn't get manga from**"):
             await event.edit("```I think this is not the right link```")
          else: 
             await event.delete()   
             await bot.send_message(event.chat_id, response.message)
             """ - cleanup chat after completed - """
             await event.client.delete_messages(conv.chat_id,
                                                [msg.id, response.id])


CMD_HELP.update({
"nhentai": 
"`.nhentai` <link / code>"
"\nUsage: view nhentai in telegra.ph XD"})