#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# (c) SpEcHiDe

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
Check your Telegram saved messages section to copy the STRING_SESSION""")
API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    session_string = client.session.save()
    saved_messages_template = """@userbotindo
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i>It is forbidden to pass this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
