# Copyright (C) 2020 MoveAngel and MinaProject
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Multifunction memes
#
# Based code + improve from AdekMaulana and aidilaryanto

import asyncio
from asyncio.exceptions import TimeoutError
import re
import random
from telethon import events
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+")


@register(outgoing=True, pattern=r"^\.q")
async def quotess(qotli):
    if qotli.fwd_from:
        return
    if not qotli.reply_to_msg_id:
        return await qotli.edit("```Reply to any user message.```")
    reply_message = await qotli.get_reply_message()
    if not reply_message.text:
        return await qotli.edit("```Reply to text message```")
    chat = "@QuotLyBot"
    if reply_message.sender.bot:
        return await qotli.edit("```Reply to actual users message.```")
    await qotli.edit("```Making a Quote```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=1031952739))
                msg = await bot.forward_messages(chat, reply_message)
                response = await response
                """ - don't spam notif - """
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await qotli.reply("```Please unblock @QuotLyBot and try again```")
            if response.text.startswith("Hi!"):
                await qotli.edit("```Can you kindly disable your forward privacy settings for good?```")
            else:
                await qotli.delete()
                await bot.forward_messages(qotli.chat_id, response.message)
                await bot.send_read_acknowledge(qotli.chat_id)
                """ - cleanup chat after completed - """
                await qotli.client.delete_messages(conv.chat_id,
                                                   [msg.id, response.id])
    except TimeoutError:
        await qotli.edit("`Error: `@QuotLyBot` is not responding!.`")


@register(outgoing=True, pattern=r'^.hz(:? |$)(.*)?')
async def hazz(hazmat):
    await hazmat.edit("`Sending information...`")
    level = hazmat.pattern_match.group(2)
    if hazmat.fwd_from:
        return
    if not hazmat.reply_to_msg_id:
        await hazmat.edit("`WoWoWo Capt!, we are not going suit a ghost!...`")
        return
    reply_message = await hazmat.get_reply_message()
    if not reply_message.media:
        await hazmat.edit("`Word can destroy anything Capt!...`")
        return
    if reply_message.sender.bot:
        await hazmat.edit("`Reply to actual user...`")
        return
    chat = "@hazmat_suit_bot"
    await hazmat.edit("```Suit Up Capt!, We are going to purge some virus...```")
    message_id_to_reply = hazmat.message.reply_to_msg_id
    msg_reply = None
    async with hazmat.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/hazmat {level}"
                msg_reply = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            elif reply_message.gif:
                m = "/hazmat"
                msg_reply = await conv.send_message(
                    m,
                    reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await hazmat.reply("`Please unblock` @hazmat_suit_bot`...`")
            return
        if response.text.startswith("I can't"):
            await hazmat.edit("`Can't handle this GIF...`")
            await hazmat.client.delete_messages(
                conv.chat_id,
                [msg.id, response.id, r.id, msg_reply.id])
            return
        else:
            downloaded_file_name = await hazmat.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await hazmat.client.send_file(
                hazmat.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            if msg_reply is not None:
                await hazmat.client.delete_messages(
                    conv.chat_id,
                    [msg.id, msg_reply.id, r.id, response.id])
            else:
                await hazmat.client.delete_messages(conv.chat_id,
                                                    [msg.id, response.id])
    await hazmat.delete()
    return os.remove(downloaded_file_name)


@register(outgoing=True, pattern=r'^.df(:? |$)([1-8])?')
async def fryerrr(fry):
    await fry.edit("`Sending information...`")
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await fry.edit("`Reply to any user message photo...`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`No image found to fry...`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Reply to actual user...`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    try:
        async with fry.client.conversation(chat) as conv:
            try:
                msg = await conv.send_message(reply_message)
                if level:
                    m = f"/deepfry {level}"
                    msg_level = await conv.send_message(
                        m,
                        reply_to=msg.id)
                    r = await conv.get_response()
                response = await conv.get_response()
                """ - don't spam notif - """
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await fry.reply("`Please unblock` @image_deepfrybot`...`")
                return
            if response.text.startswith("Forward"):
                await fry.edit("`Please disable your forward privacy setting...`")
            else:
                downloaded_file_name = await fry.client.download_media(
                    response.media,
                    TEMP_DOWNLOAD_DIRECTORY
                )
                await fry.client.send_file(
                    fry.chat_id,
                    downloaded_file_name,
                    force_document=False,
                    reply_to=message_id_to_reply
                )
                """ - cleanup chat after completed - """
                try:
                    msg_level
                except NameError:
                    await fry.client.delete_messages(conv.chat_id,
                                                     [msg.id, response.id])
                else:
                    await fry.client.delete_messages(
                        conv.chat_id,
                        [msg.id, response.id, r.id, msg_level.id])
        await fry.delete()
        return os.remove(downloaded_file_name)
    except TimeoutError:
        await fry.edit("`Error: `@image_deepfrybot` is not responding!.`")


@register(outgoing=True, pattern=r"^\.sg(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("`Reply to any user message.`")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("`Reply to actual users message.`")
        return
    await steal.edit("`Sit tight while I steal some data from NASA`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply("`Please unblock @sangmatainfo_bot and try again`")
                return
            if response.text.startswith("No records found"):
                await steal.edit("`No records found for this user`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"{response.message}")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Error: `@SangMataInfo_bot` is not responding!.`")


@register(outgoing=True, pattern=r"\.waifu(?: |$)(.*)")
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("`No text given, hence the waifu ran away.`")
            return
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}")
    await sticcers[0].click(animu.chat_id,
                            reply_to=animu.reply_to_msg_id,
                            silent=bool(animu.is_reply),
                            hide_via=True)
    await animu.delete()


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, '', inputString)


CMD_HELP.update({
    "memify":
    "`.mmf` <text_top> ; <textbottom>"
    "\nUsage: Reply a sticker/image/gif and send with cmd."
})

CMD_HELP.update({
    "hazmat":
    "`.hz` or `.hz` [flip, x2, rotate (degree), background (number), black]"
    "\nUsage: Reply to a image / sticker to suit up!"
    "\n@hazmat_suit_bot"
})

CMD_HELP.update({
    "quote":
    "`.q`"
    "\nUsage: Enhance ur text to sticker."
})

CMD_HELP.update({
    "deepfry":
    "`.df` or `.df` [level(1-8)]"
    "\nUsage: deepfry image/sticker from the reply."
    "\n@image_deepfrybot"
})


CMD_HELP.update({
    "sangmata":
    "`.sg`"
    "\nUsage: Steal ur or friend name."
})


CMD_HELP.update({
    "waifu":
    "`.waifu`"
    "\nUsage: Enchance your text with beautiful anime girl templates."
    "\n@StickerizerBot"
})
