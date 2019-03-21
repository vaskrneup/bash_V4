from subprocess import check_output, CalledProcessError


class RascleInBuilt:
    def __init__(self):
        self.show_wifi_password()

    def show_wifi_password(self):
        wifi_name_list = check_output(['netsh', 'wlan', 'show', 'profiles'],
                                      shell=True).decode('utf-8')

        wifi_data = wifi_name_list.split('\n')
        wifi_names = {}
        wifi_temp_list = []

        for names in wifi_data:
            try:
                temp = names.split(":")[1]
                if temp.strip() != "":
                    wifi_temp_list.append(temp.strip())
                    wifi_names[temp.strip()] = None
            except IndexError:
                pass

        for names in wifi_temp_list:
            try:
                wifi_pw_data = check_output(f'netsh wlan show profiles "{names.strip()}" key=clear',
                                            shell=True).decode('utf-8')
                # wifi_pw_data = check_output(['netsh', 'wlan', 'show', 'profiles',
                #                              f'{names}', 'key=clear'], shell=True).decode('utf-8')
                wifi_pw_data = wifi_pw_data.split('\n')

                for data in wifi_pw_data:
                    if data[:25].strip() == "Key Content":
                        pw = data[27:].strip()
                        wifi_names[names] = pw
            except CalledProcessError:
                pass

        for data in wifi_names:
            print(f'{data} : {wifi_names[data]}')


if __name__ == "__main__":
    RascleInBuilt()
