<h1 align="center">TelegramBot_C2C_Py</h1>
The TelegramBot C2C is a Python script that leverages the Telegram Bot API and the legimitmate use of API to establish a covert command and control (C2C) communication channel with remote agents(telegram bots as the agents). This tool enables you to execute predefined Linux, Windows, and custom commands on target systems and receive their output directly through Telegram group or chat. The use of the Telegram API allows for seamless communication without requiring Telegram to be installed on the target systems. Due to the use of the chat as the C2C interface it could run on the WAN without configration(even in VM network of NAT). The script will install all the requirements for the it run.

<h2 align="center">Features</h2>
- Command execution on remote target systems through Telegram.
- Secure communication using Telegram's API.
- Cross-platform support for Linux and Windows targets.
- Predefined commands for common OS and the ability to run custom commands of the C2C.
- Send a command to a spefic bot using: !![bot user-name] [command]

<h2 align="center">Prerequisites</h2>

<h4>Thread actor side</h4>

- python 3.x:
  - [requests library](https://requests.readthedocs.io/en/latest/) (Install
 
- Script Needs:
  - Install telegram and connect to the telegram account.
  - Create bots for the agents and main chat group.
  - Save the bot API and username.
  - Get the chat id from the API getUpdate url: https://api.telegram.org/bot[bot API token]/getUpdates, or use the get_chat_id.py to extract the chat ids.
  - Insert the bots with minimal administration privilege in the group chat.
  - Run the create_agents.py to create the script with chat id and the bot API.

<h4>Tagret side</h4>

- Python 3.x:

  - [telepot library](https://telepot.readthedocs.io/en/latest/#send-a-message) (Install using pip install telepot)

  - [urllib3 1.24.1 library](https://urllib3.readthedocs.io/en/stable/) (Install using pip3 install urllib3==1.24.1)

<h2>Usage</h2>
Clone this repository to your local machine:

```
  git clone https://github.com/yourusername/telegrambot-reverse-shell.git
  cd telegrambot-reverse-shell
  Create a Telegram bot and get your bot token:
```

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
