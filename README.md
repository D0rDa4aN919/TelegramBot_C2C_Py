# TelegramBot_C2C_Tool
C2C tool that use the chat of telegram group as the C2C interface. The bots as agents that execute the command and send the result.

TelegramBot Reverse Shell Tool
The TelegramBot Reverse Shell Tool is a Python script that leverages the Telegram Bot API to establish a covert command and control (C2C) communication channel with remote agents. This tool enables you to execute predefined Linux, Windows, and custom commands on target systems and receive their output directly through Telegram. The use of the Telegram API allows for seamless communication without requiring Telegram to be installed on the target systems.

Features
Command execution on remote target systems through Telegram.
Secure communication using Telegram's API.
Cross-platform support for Linux and Windows targets.
Predefined commands for common tasks and the ability to run custom commands.
Prerequisites
Python 3.x
python-telegram-bot library (Install using pip install python-telegram-bot)
Usage
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/telegrambot-reverse-shell.git
cd telegrambot-reverse-shell
Create a Telegram bot and get your bot token:

Follow the official Telegram guide to create a new bot and obtain its token.

Get the chat ID of the group you want to work with:

You can use tools like @userinfobot to get the chat ID of your group.

Edit the config.py file:

Open the config.py file and replace the placeholders with your bot token and group chat ID:

python
Copy code
BOT_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'
Run the agent on the target system:

Execute the agent script on the target system. Depending on the system, run either agent_linux.py or agent_windows.py:

bash
Copy code
# For Linux
python agent_linux.py

# For Windows
python agent_windows.py
The agent will now be listening for commands from the Telegram group.

Interact with the agent:

In the Telegram group, send commands prefixed with !linux, !windows, or !custom to execute predefined Linux, Windows, or custom commands respectively. The agent will execute the command and reply with the output.

Security Considerations
Use responsibly: This tool is intended for educational and ethical purposes. Do not use it for malicious intent.
Secure your bot token: Keep your bot token secret and do not share it publicly.
Risk of exposure: While the Telegram API offers encryption, there is always a risk of exposure. Avoid sending sensitive information through the tool.
Legality: Ensure that you comply with local laws and regulations before using this tool.
Disclaimer
This tool is provided for educational purposes only. The authors are not responsible for any misuse or damage caused by this tool. Use at your own risk.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
