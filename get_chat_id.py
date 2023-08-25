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
