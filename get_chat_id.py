##############################################################################
# TelegramBot_C2C_Py - get_chat_id.py - Python Script
# Description: Fliter and extract the chat id by the chat name and the bot API token
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import requests

# Input the chat name to use
CHAT = input("Enter chat name: ")
# Input the bot API token to use
TOKEN = input("Enter the API token of the boot: ")
end = False
# will loop the bot info to extract the chat id, username, and text 
while not end:
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates").json()

    if response["ok"] is False:
        print("There was an error with the API token.")
        exit(1)

    check = True
    chat_ids = {}
    number = 0
    for line in response["result"]:
        if "message" in line and "chat" in line["message"]:
            chat = line["message"]["chat"]
            if "title" in chat and chat["title"] == CHAT:
                if "text" in line["message"]:
                    check = False
                    chat_ids[f"{CHAT}{number}"] = {
                        "chat_id": chat["id"],
                        "username": f'{line["message"]["from"]["username"]}',
                        "text": f'{line["message"]["text"]}'}
                    number += 1
    number = 0
    if check:
        print("No chats found with the specified title.")
    else:
        checker = []
        for key in list(chat_ids.keys())[::-1]:
            if chat_ids[key]["chat_id"] not in checker:
                print(f"{CHAT}: {chat_ids[key]['chat_id']}, The user: {chat_ids[key]['username']},Send this message: {chat_ids[key]['text']}.")
                checker.append(chat_ids[key]["chat_id"])
        end = True

# License Information
# This script is open-source and released under the MIT License.
# MIT License
# Copyright (c) 2023 Dor Dahan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# or visit https://github.com/D0rDa4aN919/TelegramBot_C2C_Py.
