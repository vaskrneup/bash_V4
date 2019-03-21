from os import path
from shutil import rmtree

current_file_path = path.dirname(path.abspath(__file__))  # Grabs current file path !

working_path = current_file_path.split("\\")
working_path.pop()

working_path = path.join("\\".join(working_path), 'ter_update_temp')

rmtree(working_path)
