# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        string = "Specify which module do you want help for !!\n**Usage:** `.help` <module name>\n\n"
        for i in sorted(CMD_HELP):
            string += "`" + str(i) + "`"
            string += "\t\t\t||\t\t\t "
        await event.edit(string)
