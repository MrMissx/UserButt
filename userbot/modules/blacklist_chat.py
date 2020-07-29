# Copyright (C) 2020 KeselekPermen69.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""all userbot event handler will ignored in blacklisted chat."""

import io
from userbot import CMD_HELP
from userbot.events import register
import userbot.modules.sql_helper.chat_blacklist_sql as bl_sql


@register(incoming=True, blacklist_chat=False, pattern=r"^.addblchat (.*)")
async def add_chat_blacklist(new_chatlist):
    """Add curent chat or input string to blacklist chat"""
    chat = new_chatlist.pattern_match.group(1)
    if chat == "":
        chat = new_chatlist.chat_id
    bl_sql.add_chatlist(chat)
    await new_chatlist.edit(f"`{chat}` has been added to userbot chat blacklist.")


@register(incoming=True, blacklist_chat=False, pattern=r"^.unblchat (.*)")
async def rm_chat_blacklist(rm_chatlist):
    chat = rm_chatlist.pattern_match.group(1)
    if chat == "":
        chat = rm_chatlist.chat_id

    if bl_sql.rm_chatlist(chat) is True:
        await rm_chatlist.edit(f"`{chat}` has been removed from userbot chat blacklist.")
    else:
        await rm_chatlist.edit(f"Chat {chat} isn't blacklisted.")


@register(incoming=True, pattern=r"^.blchats (.*)")
async def get_chat_blacklist(rm_chatlist):
    chat_list = bl_sql.get_chatlist()
    output = "Blacklisted chat for userbot:\n"
    if len(chat_list) > 0:
        for blacklisted in chat_list:
            output += f"`{blacklisted}`\n"
    else:
        await rm_chatlist.edit("`there are no current chat blacklist for userbot`")

    if len(chat_list) > 4096:
        with io.BytesIO(str.encode(output)) as output_file:
            output_file = "chat_blacklist.txt"
            await rm_chatlist.client.send_file(
                rm_chatlist.chat_id,
                output_file,
                force_document=True,
                allow_cache=False,
                caption="All userbot blacklisted chat"
            )
            await rm_chatlist.delete()
    else:
        await rm_chatlist.edit(output)


CMD_HELP.update({
    "ChatBlacklist":
    "`.addblchat` <chatid>"
    "\nUsage: add curent chat or input chat to userbot blacklist"
    "\n\n`.unblchat` <chatid>"
    "\nUsage: remove userbot blacklisted chat"
    "\n\n`.blchats`"
    "\nUsage: list all blacklisted chat"
    "\n\n* `.addblchat` and `.unblchat` is not affected by blacklisted chat"
    "\n*This module is currently in beta and may not work properly.*"
})