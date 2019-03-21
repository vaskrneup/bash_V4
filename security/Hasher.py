from os import path


class Hash:
    def __init__(self, command=None, split_command=None, cwd=None):
        self.command = command
        self.split_command = split_command

        self.current_working_dir = cwd  # Gets current working directory !

        self.input_file_name = ""
        self.output_file_name = ""
        self.overwrite_files = False
        self.input_string = ""
        self.pin = 532389

    def execute(self):
        command_space_split = self.command.split(" ")

        if command_space_split[0] == "hash":
            if path.isfile(f"{self.current_working_dir}\\{command_space_split[1]}"):
                self.input_file_name = command_space_split[1]
                try:
                    self.output_file_name = command_space_split[2]
                except IndexError:
                    self.input_file_name = self.output_file_name
                try:
                    self.pin = int(command_space_split[3])
                except IndexError:
                    self.pin = 8258
                try:
                    if command_space_split[4] == "ow":
                        self.overwrite_files = True
                except IndexError:
                    pass
                return self.hash_file()
            else:
                return True

        elif command_space_split[0].strip() == "unhash":
            if path.isfile(f"{self.current_working_dir}\\{command_space_split[1]}"):
                self.input_file_name = command_space_split[1]
                
                try:
                    self.output_file_name = command_space_split[2]
                except IndexError:
                    self.input_file_name = self.output_file_name
                try:
                    self.pin = int(command_space_split[3])
                except IndexError:
                    self.pin = 8258
                except ValueError:
                    print("Pin must be a positive integer!")
                    print("Type -h at last for help!")
                    return True
                try:
                    if command_space_split[4] == "ow":
                        self.overwrite_files = True
                except IndexError:
                    pass
                return self.unhash_file()

        else:
            return False

    def unhash_string(self):
        # input_string = str(input_string)
        # input_string = input_string.split("-")
        int_count = 1
        first_term = 3

        self.input_string = self.input_string.split('-')

        output_data = ""
        for data in self.input_string:
            count = first_term + (int_count - 1) * int(self.pin)
            code_string = str(int(data) - int(self.pin) - count)
            output_data += chr(int(code_string))
            int_count += 1

        return output_data

    def hash_string(self):
        int_count = 1
        final = ""
        first_term = 3

        for data in self.input_string:
            # print(f"{type(first_term)}\n{type(int_count-1)}\n{type(self.pin)}")
            count = first_term + (int_count - 1) * self.pin
            code_string = str(ord(data) + self.pin + count)
            final += str(code_string) + "-"
            int_count += 1

        return final

    def unhash_file(self):
        output_file = f"{self.current_working_dir}\\{self.output_file_name}"

        def writer():
            read_file = open(f"{self.current_working_dir}\\{self.input_file_name}", 'r')
            write_file = open(f"{self.current_working_dir}\\{self.output_file_name}", 'a')

            for line in read_file:
                self.input_string = line
                un_hashed_str = self.unhash_string()
                write_file.write(f"{un_hashed_str[:-1]}\n")
            read_file.close()
            write_file.close()
            print("Hashed !")
            return True

        if self.input_file_name == self.output_file_name or self.output_file_name == path.isfile(output_file):
            if self.overwrite_files:
                return writer()
            else:
                print("File cant be overwritten !")
                return True
        else:
            return writer()

    def hash_file(self):
        output_file = f"{self.current_working_dir}\\{self.output_file_name}"

        def writer():
            read_file = open(f"{self.current_working_dir}\\{self.input_file_name}", 'r')
            write_file = open(f"{self.current_working_dir}\\{self.output_file_name}", 'a')

            for line in read_file:
                self.input_string = line
                hashed_str = self.hash_string()
                write_file.write(f"{hashed_str[:-1]}\n")
            read_file.close()
            write_file.close()
            print("Hashed !")
            return True

        if self.input_file_name == self.output_file_name or self.output_file_name == path.isfile(output_file):
            if self.overwrite_files:
                return writer()
            else:
                print("File cant be overwritten !")
                return True
        else:
            return writer()


if __name__ == "__main__":
    Hash()
