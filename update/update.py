from subprocess import check_output, CalledProcessError
from os import listdir, chdir, remove, system, path
from termcolor import colored
from shutil import copytree, copy, rmtree
from time import sleep as pause_for


class Update:
    def __init__(self, cwd, base_dir, current_app_version):
        self.base_dir = base_dir  # gets base dir !
        self.current_working_dir = cwd  # gets last working dir !

        chdir(self.base_dir)  # Changes working dir to base dir !
        self.current_files_in_dir = listdir(self.base_dir)  # Grabs all files in current dir !

        self.current_version = current_app_version  # grabs bash current version !

    def check_update(self):
        # try to grab url for new version !
        try:
            # checks if url for new version exist !
            check_output(['git', 'clone',
                          f'https://github.com/rascledeveloper/'
                          f'bash_V{int(self.current_version) + 1}', 'ter_update_temp'],
                         shell=True)
            print('\n\n')
            print("")
            system('color')  # creates environment for colored text !
            print(colored("Update successfully downloaded !\n", 'green'))

            pause_for(3)  # for letting git complete whatever it needs to !

            self.remove_old_files_and_folders()  # runs function !
            self.copy_new_files_and_folders()  # runs function !
            self.del_temporary_update_files()  # runs function !

            print("UPDATE SUCCESSFUL !")
            print("QUITTING TERMINAL !\nPLEASE OPEN TERMINAL AGAIN !")
            pause_for(4)  # for letting git complete whatever it needs to !
            quit()  # quits the bash so updated bash can be opened !
        except CalledProcessError:  # handles if no update are available !
            system('color')
            print(colored("No new updates are available !\n", 'red'))
            chdir(self.current_working_dir)  # changes dir to where it was before !
        else:
            print()

    # removes old files and folders !
    def remove_old_files_and_folders(self):
        # loops through all old folders !
        for folder in self.current_files_in_dir:
            # grabs root path of each folder !
            path_of_files = f"{self.base_dir}\\{folder}"

            # checks if data is folder or file !
            if path.isdir(path_of_files):
                print(colored(f"[~] DELETE FOLDER --- {path_of_files}", 'red'))
                rmtree(path_of_files)  # removes non empty folder !
            else:
                print(colored(f"[~] DELETE FILE --- {path_of_files}", 'red'))
                remove(f"{self.base_dir}\\{folder}")  # removes empty folder !
        print(colored("\n[*] OLD FILES DELETED !\n", 'red'))

    # copy new files and folder to base dir !
    def copy_new_files_and_folders(self):
        # grabs dir of files to be copied !
        update_file_dir = f"{self.base_dir}\\ter_update_temp"
        # list files in the update package !
        current_dir_files = listdir(update_file_dir)
        # removes temp folder so that it won't get copied !
        current_dir_files.remove(".git")

        # loops through all files and folder to be copied !
        for folder in current_dir_files:
            # grabs root path of the folder !
            folder_dir = f"{update_file_dir}\\{folder}"

            # checks if data id folder|dir !
            if path.isdir(folder_dir):
                # copies to base path !
                copytree(folder_dir, f"{self.base_dir}\\{folder}")
                print(colored(f"[~] COPY FOLDER --- {folder_dir}", 'green'))
            else:
                # copies to base path !
                copy(folder_dir, f"{self.base_dir}")
                print(colored(f"[~] COPY FILE --- {folder_dir}", 'green'))

        print(colored("\n[*] NEW FILES COPIED !\n", 'green'))

    # removes files after updating !
    def del_temporary_update_files(self):
        # creates root path to temporary update files !
        files_inside_update_folder = listdir(f"{self.base_dir}\\ter_update_temp")

        # removes temp folder that may cause error !
        if ".git" in files_inside_update_folder:
            files_inside_update_folder.remove(".git")

        # loops through files and folder in update dir !
        for data in files_inside_update_folder:
            # creates base dir for data to be removed !
            data_to_remove = f"{self.base_dir}\\ter_update_temp\\{data}"

            # checks if data is folder|dir !
            if path.isdir(data_to_remove):
                # removes the non empty dir !
                rmtree(data_to_remove)
                print(colored(f"[~] REMOVING INSTALLATION FOLDER --- {data_to_remove}", 'red'))
            else:
                # removes the file !
                remove(data_to_remove)
                print(colored(f"[~] REMOVING INSTALLATION FILE --- {data_to_remove}", 'red'))


if __name__ == "__main__":
    Update()
