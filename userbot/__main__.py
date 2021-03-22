# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot start point"""

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot, BOTLOG_CHATID
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    "Congratulations, your userbot is now running !!"
    "Test it by type .on or .alive in any chat."
    "for further assistance, head to https://t.me/userbotindo")

if not BOTLOG_CHATID:
    LOGS.warning(
        "Yout BOTLOG_CHATID isn't set yet."
        "this variable is highly recomended to fill to make sure"
        "all errors go to your log chat not current chat and considered as a spammer.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
