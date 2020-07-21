# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# (c) Spechide - UniBorg
# Port From UniBorg to UserBot by @afdulfauzan

from telethon.tl import functions
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.create (b|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """For .create command, Creating New Group & Channel"""
    if grop.text[0].isalpha() or grop.text[0] in ("/", "#", "@", "!"):
        return
    if grop.fwd_from:
        return
    type_of_group = grop.pattern_match.group(1)
    group_name = grop.pattern_match.group(2)
    if type_of_group == "b":
        try:
            result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@MissRose_bot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Your {0} Group Created Successfully. Click [{0}]({1}) to join".format(group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))
    elif type_of_group in ("g", "c"):
        try:
            r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="Welcome to this Channel",
                megagroup=not bool(type_of_group == "c")
            ))
            created_chat_id = r.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Your {0} Group/Channel Created Successfully. Click [{0}]({1}) to join".format(group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))

CMD_HELP.update({
    "create":
    "\n\n`.create g` <group name>"
    "\nUsage: Create a Private Group."
    "\n\n`.create b` <group name>"
    "\nUsage: Create a Group with Bot."
    "\n\n`.create c` <channel name>"
    "\nUsage: Create a Channel."
})
