# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

# port to userbot from uniborg by @keselekpermen69


import io
import re
import userbot.modules.sql_helper.blacklist_sql as sql
from asyncio import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(incoming=True, disable_edited=True, disable_errors=True)
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply("I do not have DELETE permission in this chat")
                await sleep(1)
                await event.delete()
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@register(outgoing=True, pattern="^.addbl(?: |$)(.*)")
async def on_add_black_list(addbl):
    text = addbl.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(addbl.chat_id, trigger.lower())
    await addbl.edit("`Added` **{}** `to the blacklist in the current chat`".format(text))


@register(outgoing=True, pattern="^.listbl(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`There are no blacklist in current chat.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)


@register(outgoing=True, pattern="^.rmbl(?: |$)(.*)")
async def on_delete_blacklist(rmbl):
    text = rmbl.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(rmbl.chat_id, trigger.lower()):
            successful += 1
    if not successful:
        await rmbl.edit("`Blacklist` **{}** `doesn't exist.`".format(text))
    else:
        await rmbl.edit("`Blacklist` **{}** `was deleted successfully`".format(text))

CMD_HELP.update({"blacklist": "`.listbl`"
                 "\nUsage: Lists all active userbot blacklist in a chat."
                 "\n\n`.addbl` <keyword>"
                 "\nUsage: Saves the message to the 'blacklist keyword'."
                 "\nThe bot will delete to the message whenever 'blacklist keyword' is mentioned."
                 "\n\n`.rmbl` <keyword>"
                 "\nUsage: Stops the specified blacklist."})
