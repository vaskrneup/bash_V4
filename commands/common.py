from os import system, path
from distutils import spawn


class Common:
    def __init__(self, command=None, split_command_minus=None, split_command_space=None, cwd=None, base_dir=None):
        self.command = command  # Stores command received !
        self.split_command_minus = split_command_minus  # Stores splitted command using '-'!
        self.split_command_space = split_command_space  # Stores splitted command using '<SPACE>'!
        self.current_working_dir = cwd  # Current working directory !
        self.base_dir = base_dir  # Base directory of the file !
        self.command_file_dir = f"{path.join(base_dir, 'files')}\\63428278.txt"  # Command dir !

    # reroutes commands to their respective functions !
    def execute(self):
        try:
            if self.command == "clear":
                return Common.clear()
            elif self.command.split(' ')[0].strip() == "history":
                return self.history()
            elif self.command.split(" ")[0] == "shutdown":
                return self.shutdown()
            elif self.command == "rm history":
                return self.del_history()
            elif self.command.split(' ')[0] == "installed":
                pass
            elif self.command.split(' ')[0].strip() == "nano":
                return self.nano()
            elif self.command == "new bash":
                return self.new_bash()
            elif self.command == "explorer":
                return self.open_file_manager()
            elif self.command == "quit" or self.command == "exit":
                raise OSError  # Raise value Error so Exiting is Easy !
            elif self.command[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']:
                if '^' in [letters for letters in self.command]:
                    self.command = self.command.replace('^', "**")
                return self.calculator()
            else:
                return False

        except IndexError:
            pass

    # opens file manager in path of cwd !
    def open_file_manager(self):
        system(f"start {self.current_working_dir}")
        return True

    # Calculates Value !
    def calculator(self):
        try:
            exec(f"print({self.command})")
            return True
        except:
            return False

    # Starts new bash !
    def new_bash(self):
        system(f"start {self.base_dir}/ter.bat")
        return True

    # Opens text file in notepad to edit !
    def nano(self):
        try:
            file_name = self.command.split(' ')[1]  # splits out file name !
            # Checks if file exists !
            if path.isfile(f"{self.current_working_dir}\\{file_name.strip()}"):
                # open's the file !
                system(f"start notepad {self.current_working_dir}\\{file_name}")
            else:
                print("File Doesnt exist !")
        # If no argument is given then run this code !
        except IndexError:
            print("File name not given !")
        return True

    # Removes everything from the command file !
    def del_history(self):
        working_file = open(f"{self.command_file_dir}", 'w')  # initiates new command file !
        working_file.close()  # Closes command file !
        print("History removed !")
        return True

    # outputs history !
    def history(self):
        working_file = open(f"{self.command_file_dir}", 'r')  # opens command history file !
        # creates list of command in history file !
        used_commands = [command for command in working_file]
        # Close command history file !
        working_file.close()

        # Captures additional argument !
        try:
            # Captures how many commands to show !
            range_of_commands = self.command.split(' ')[1]
            # Start of command !
            start = len(used_commands) - 1
            # End of command !
            end = start - int(range_of_commands)
            # loops through last commands !
            for i in range(start, end, -1):
                # prints commands !
                print((used_commands[i]).strip())
        # if no argument is given then print all commands !
        except IndexError:
            # Loops through last index to backward !
            for i in range(len(used_commands), 0, -1):
                # prints command from last to first !
                print(used_commands[i])
        return True

    # Shutdowns device !
    def shutdown(self):
        # grab additional argument !
        try:
            # grabs timer !
            timer = self.command.split(" ")[1]
            # shutdowns according after timer seconds !
            system(f"shutdown -s -t {timer}")
        # if no additional argument is given then use this !
        except IndexError:
            # shutdowns after 3 seconds !
            system('shutdown -s -t 3')

        return True

    # Checks if an app is installed !
    @staticmethod
    def is_tool():
        # checks if app is installed or not !
        if spawn.find_executable("apple") is not None:
            print("Yes !")

    # clears the screen !
    @staticmethod
    def clear():
        system('cls')  # Clears the screen !
        return True


if __name__ == "__main__":
    Common()
