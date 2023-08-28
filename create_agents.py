##############################################################################
# TelegramBot_C2C_Py - create_agents.py - Python Script
# Description: Will create bot agents script by the chat id and the bot API tokens
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import os
import re
import shutil


def main():
    """
    The main start and variables that will use later in the script
    """
    end = True
    while end:
        try:
            bot_amount = int(input("How much telegram bot agents do you use: "))
        except ValueError as e:
            print(f"Error: {e}")
            continue
        try:
            chat_id = input("Enter the chat ID of the telegram bot agents do you use as interface: ")
        except Exception as e:
            print(f"Error: {e}")
            continue
        end = False
    creation(bot_amount, chat_id)


def creation(bot_amount: int, chat_id: str):
    """
    Create the script using the agents/shell.py file, the chat id of the chat, and the bot token.
    :param bot_amount: The bot amount
    :param chat_id: The telegram chat id
    """
    if os.path.isdir("./ready_agents"):
        if len(os.listdir("./ready_agents")) > 0:
            shutil.rmtree("./ready_agents")
    if not os.path.isdir("./ready_agents"):
        os.makedirs("./ready_agents")
    for num in range(1, bot_amount + 1):
        with open("agents/shell.py", "r") as file:
            text = file.readlines()
        final_text = ""
        while True:
            TOKEN = input("Enter the telegram bot API Token of the telegram bot agents do you: ")
            if not is_valid_token(TOKEN):
                print("This is not a valid token.\nPlease enter the right telegram bot API.")
                continue
            break
        for line in text:
            if "CHAT_ID = " in line:
                line = f'CHAT_ID = "{chat_id}"\n'
            if "TOKEN = " in line:
                line = f'TOKEN = "{TOKEN}"\n'
            final_text += line
        with open(f"ready_agents/shell_id_{TOKEN.split(':')[0]}.py", "w") as file:
            file.write(final_text)
    print("The bot agent scripts are ready and exiting in ./ready_agents directory!.")
    print("Install telegram for the C2 interface.")


def is_valid_token(token: str):
    """
    Check the telegram bot API tokens are in the right format: <bot_id>:<bot_token>
    :param token: The api token to check
    """
    pattern = r'^\d+:[\w-]+$'
    return re.match(pattern, token) is not None


if __name__ == "__main__":
    main()
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
