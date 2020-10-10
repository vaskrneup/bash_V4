"""
** = Anything written after this must be taken into consideration !
@ = Referring to something else !
 pip install PyPDF2
"""
# System Modules !
from os import system, path, getcwd, mkdir, chdir, remove
from shutil import copy
from time import sleep
try:
    from send2trash import send2trash
    from requests import get, ConnectionError
except ModuleNotFoundError:
    install_module = input("some modules are missing would you like to install it ?[y|n] : ")
    if install_module.lower() == "y":
        system("pip3 install termcolor")
        system("pip3 install send2trash")
        system("pip3 install requests")
        from requests import get, ConnectionError
        from send2trash import send2trash
    else:
        quit()
from subprocess import check_output, CalledProcessError
# print(colored('hello', 'red'), colored('world', 'green'))
# Custom module !
from commands import common, dirs, file, function, rascle
from help.help import HelpFinder
# from help import help_dirs, help_file, help_function
from security import Hasher
from security import errors as custom_error
from styleMain.color import *
from update.update import Update


class Bash:
    def __init__(self, error=False, command=None, ctrl_exit=False):
        self.CURRENT_APP_VERSION = '4'
        system('color')  # creates environment for printing colored text !

        # =====================EXTRA ARGUMENT CHECKING===========================
        if not ctrl_exit and command is None:  # Checks if CTRL + C is NOT PRESSED and command is not directly runned !
            common.Common.clear()  # Clears the screen !

        if error:  # CHECKS IF any ERROR occurred and script needs to restart !
            red("Error detected so restarted !\n"
                "We will try to fix these errors as soon as possible !\n")

        if command is None:  # CHECKS IF script is runned with some commands !
            print(yellow("Developed by vaskr | GITHUB : 'RascleDeveloper'", attrs=["underline"]))
            print(yellow("Windows terminal made easy !\n", attrs=["underline"]))
        # ====================EXTRA ARGUMENT END==================================

        # ===========================DECLARATIONS=================================
        self.command = ""  # keeps input from user !
        self.split_command_temp = ""  # Splits command into list using '-' !
        self.split_command_minus = ""  # Splits String using '-' and store store the new list !
        self.split_command_space = ""  # Splits String using '<SPACE>' and store store the new list !

        self.terminal_title = "BN Bash"  # sets title of the bash !
        self.bash_bg_color = "blue"  # sets bash background color to black **Must be color name @CLASS Color
        self.bash_fg_color = "red"  # sets bash foreground color to green **Must be color name @CLASS Color

        self.logged_in = None  # File for verifying user login !

        self.current_file_path = path.dirname(path.abspath(__file__))  # Grabs current file path !
        self.TYPED_COMMANDS_FILE_PATH = path.join(self.current_file_path, "files/63428278.txt")  # FILE for saving
        self.current_working_dir = getcwd()  # Gets current working directory !

        self.bash_formatting_before_login = f"@LoginConsole ({self.current_working_dir})$ "  # Sets bash for new users !
        self.bash_formatting_root = f"# ({self.current_working_dir})$ "  # Sets bash for root user !
        self.bash_formatting_non_root = f"~ ({self.current_working_dir}$ )"  # Sets bash for non root user !

        self.temp_first = None  # STORES temporary data !
        # =========================DECLARATIONS END=================================

        if path.isdir(f"{self.current_file_path}\\ter_update_temp"):
            send2trash(f"{self.current_file_path}\\ter_update_temp")

        # =========================RUNS COMMANDS IF THEY ARE PASSED=================
        if command is not None:
            for commands in command:  # Loops through all commands !
                self.command = commands  # if command have some value set input to that !
                self.startup_setup_first()  # runs initial setup !
                self.startup_setup_second()  # runs initial setup !
                self.pass_commands()  # runs commands !
                print()
        # =========================END COMMAND PASSING==============================

        self.command_handler()  # run commands handler !

    def startup_setup_first(self):  # Checks initial setup, load initial data, corrects files !
        if not path.isdir(f"{self.current_file_path}\\CDF"):  # CHECKS IF CDF DIRECTORY EXIST OR NOT !
            mkdir(f"{self.current_file_path}\\CDF")  # MAKES CDF FOLDER !
        if not path.isdir(f"{self.current_file_path}\\files"):  # CHECKS IF DIRECTORY files EXIST OR NOT !
            mkdir(f"{self.current_file_path}\\files")  # MAKES files FOLDER !

        save_bash_commands = open(self.TYPED_COMMANDS_FILE_PATH, 'a')  # Open COMMAND HISTORY file for writing into it !
        save_bash_commands.write(f"{self.command}\n")  # Saves typed commands to file !
        save_bash_commands.close()  # Close COMMANDS HISTORY FILE

        self.split_command_temp = self.command.split("-")  # Splits command using using '-' !
        # Init - list !
        # split command using - and store the list !
        self.split_command_minus = self.command.split("-")
        # Init - list !
        # split command using <SPACE> and store the list !
        self.split_command_space = self.command.split(" ")  # Init <SPACE> list !

        # for words in self.split_command_temp:  # Loops through words in splited input command !
        #     self.split_command_minus.append(words.strip())  # Removes spaces from words !

    def startup_setup_second(self):  # Sets how console looks
        # Sets bash for new users !
        self.bash_formatting_before_login = f"@LoginConsole ({self.current_working_dir})$ "
        # Sets bash for root user !"
        self.bash_formatting_root = f"{green('@', attrs=['dark'])}" \
            f" {green(self.current_working_dir)} {red('$')} "
        # Sets bash for non root user !
        self.bash_formatting_non_root = f"~ ({self.current_working_dir}$ )"

    def command_handler(self):  # Reroutes all the command for better execution !
        #  Loops until user doesn't EXIT !
        while True:
            try:
                chdir(self.current_working_dir)  # Changes APP directory NOT VIRTUAL ! 

                self.startup_setup_second()  # runs second initial setup !
                self.command = input(self.bash_formatting_root)  # Takes command from user !

                self.startup_setup_first()  # runs second initial setup !
                if self.command.strip() != "":  # checks if command is NOT NULL
                    # ----------------------COMMAND PASSING-------------------
                    self.pass_commands()  # Pass commands through other modules !
                print()
            except KeyboardInterrupt:  # If someone types CTRL C then it catches !
                print(green("\n[~]"), red("STOPPED"))

    def pass_commands(self):
        # TRUE IS RETURNED JUST FOR READABILITY !

        # =================================HELP========================================
        # Using this for checking if help text is required !
        if self.command == "help" or 'h' in [argument for argument in self.split_command_minus]:
            HelpFinder(self.command, self.split_command_minus, self.split_command_space,
                       self.current_file_path).execute()  # Runs help module !
            return True
        # ================================END HELP====================================
        else:
            # ===========================PASS COMMANDS TO MODULE=================================
            # IF NO HELP is REQUIRED run these commands !

            # Grabbing output for changing directory !
            output_grabbing = dirs.Dirs(self.command, self.split_command_minus, self.split_command_space,
                                        self.current_working_dir, self.current_file_path).execute()

            # CHECKS MOST USED COMMANDS !
            if common.Common(self.command, self.split_command_minus, self.split_command_space,
                             self.current_working_dir, self.current_file_path).execute():
                # print("1")
                return True
            elif self.command == "show wifi password":
                rascle.RascleInBuilt()
            # CHECKS COMMANDS RELATED TO DIRECTORY !
            elif output_grabbing:
                # Checks if text is returned or bool value !
                if type(output_grabbing) != bool:
                    # Change current working dir to the grabbed value !
                    self.current_working_dir = output_grabbing
                # print("2")
                return True
            # CHECKS FILE RELATED COMMANDS !
            elif file.File(self.command, self.split_command_minus, self.split_command_space,
                           self.current_working_dir, self.current_file_path).execute():
                # print("3")
                return True
            # CHECKS IF CUSTOM DEFINED FUNCTION IS CREATED OR RUNNED !
            elif function.Function(self.command, self.split_command_minus, self.split_command_space,
                                   self.current_working_dir, self.current_file_path).execute():
                # print("4")
                return True
            # CHECKS IF FILE IS ASKED TO HASH OR NOT !
            elif Hasher.Hash(self.command, self.split_command_minus, self.current_working_dir).execute():
                # print("5")
                return True
            # ========================END PASS COMMANDS TO MODULE============================
            else:
                # ======================LONG COMMANDS================
                # checks for update !
                if self.command == "update":
                    # checks for internet connection !
                    if Bash.connected_to_internet():
                        # CHECKS IF GIT is installed or not !
                        try:
                            # IF GIT IS INSTALLED THEN

                            # Runs command in terminal !
                            check_output(['git', 'help'])
                            # Runs update !
                            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            Update(self.current_working_dir, self.current_file_path, self.CURRENT_APP_VERSION).check_update()
                            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                        # RUNS THIS IF GIT is NOT INSTALLED !
                        except CalledProcessError:
                            installed = input("Have you installed git [y/n] : ")
                            if installed == "y":
                                help_for_installation_of_git = input("PLEASE REINSTALL GIT AND GO FOR DEFAULT SETTINGS"
                                                                     " ! DOWNLOAD GITHUB ? [y/n] : ")
                                if help_for_installation_of_git == 'y':
                                    # DOWNLOADS GIT directly from default browser !
                                    system('start https://git-scm.com/download/win')
                                    print("PLEASE RESTART THE BASH AFTER INSTALLING GIT !")
                            else:

                                install_git = input("type 'y' to go for download page of git : ")
                                if install_git == "y":
                                    print(yellow("LEAVE EVERYTHING AS DEFAULT DURING INSTALLATION !",
                                                 attrs=['bold', 'underline', 'dark']))
                                    # SLEEP IS KEPT FOR NOTIFICATIONS !
                                    sleep(3)  # Waits for 3 seconds before opening browser !
                                    # DOWNLOADS GIT directly from default browser !
                                    system('start https://git-scm.com/download/win')
                                    print("PLEASE RESTART THE BASH AFTER INSTALLING GIT !")
                    else:
                        print("Please make sure you are connected to the internet !")

                # Checks for internet connection !
                elif self.command == "is internet working":
                    if Bash.connected_to_internet():  # Checks for internet connection !
                        print("Yes, Internet is working !")
                    else:
                        print("No, Internet is not working !")

                # ADDS TER TO LIST OF COMMANDS SO THAT IT CAN BE RUNNED INSTEAD OF CMD !
                elif self.command == "ADDTOPATH":
                    print("example: cmd, bash !")
                    print("DONT USE cmd IT WILL OVER WRITE PATH OF CMD !\n")
                    print("LEAVE IT BLANK FOR 'ter' !")

                    name_of_command = input('command to activate ter from any path : ')
                    if name_of_command.strip() == "":  # removes spaces from input !
                        name_of_command = "ter"  # sets default command to ter !
                    # makes file to copy in SYS32
                    path_maker = open(f'{name_of_command}.bat', 'w')
                    # write required commands in file !
                    path_maker.write(f'@echo off\ntitle Bash\n\npython {self.current_file_path}\\{name_of_command}.bat')
                    # close file
                    path_maker.close()
                    # Try to copy file in SYS32 !
                    try:
                        # COPY FILE TO SYSTEM32 !
                        copy(f'{self.current_file_path}\\{name_of_command}.bat', 'C:\\WINDOWS\\system32')
                        # DISPLAY HELP MESSAGE !
                        print(f"\nNOW YOU CAN USE {name_of_command} ANYWHERE WHERE YOU COULD HAVE USED CMD !")
                    # IF cant copy display following message !
                    except PermissionError:
                        print("You need to run script with administrative permission to ADD ter to path !")
                        print("\nRIGHT CLICK ON ter.bat in the place where extracted !\n"
                              "Then click on run as administrator")
                    if name_of_command != "ter":  # checks if default command is used or not !
                        # if default command is not used then remove the file !
                        remove(f'{self.current_file_path}\\{name_of_command}.bat')
                # ==========================END LONG COMMANDS=================================

                # IF NO COMMANDS MATCHED THEN RUN COMMAND IN CMD
                else:
                    # CHECK FOR ADDITIONAL ARGUMENT !
                    try:
                        command = self.command.split("&")  # split with & !
                        self.temp_first = command[1]  # extracts additional argument !
                        command.pop()  # removes additional argument !
                        # store command without additional argument !
                        self.command = " ".join(command).strip()
                    # if no additional argument is found !
                    except IndexError:
                        pass
                    # try to print colored text with additional argument !
                    try:
                        if self.split_command_space[0].strip() == "python":
                            raise custom_error.PythonIsCalled
                        # Checks for output !
                        output = check_output(self.split_command_space)
                        # makes output colored !
                        output = cyan(output)
                        # extract line from output !
                        output = output.split('\\n')

                        # =================START CHECKING FOR ARGUMENT===============
                        if self.temp_first == "c":
                            # sets temporary variable to NONE
                            self.temp_first = None
                            count = 0

                            # print with line number infront of output !
                            for data in output:
                                count += 1
                                # prints count <SPACE> <OUTPUT without last two string> !
                                print(f"[{count}] {data[:-2]}")
                        # =================END CHECKING FOR ARGUMENT===================
                        else:
                            # If no command then print [*] infront of line !
                            for data in output:
                                # prints count <SPACE> <OUTPUT without last two string>
                                print(f"[*] {data[:-2]}")
                    # if cant get output then run directly without any styling !
                    except:
                        system(self.command)

    @staticmethod
    def connected_to_internet(url='http://www.google.com/', timeout=5):
        # try to get data from requested url for 5 seconds !
        try:
            get(url, timeout=timeout)
            return True
        # if cant get reply then run this !
        except ConnectionError:
            return False


if __name__ == "__main__":
    # noinspection PyBroadException
    # Bash()
    try:
        Bash()
    except OSError:
        quit()
    except:
        Bash(error=True)
