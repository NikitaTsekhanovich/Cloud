import create_folder as cr
import upload_file as uf
import download_file as df
import get_information as gi


def select_contracts(url, headers, token, application):
    options = ['1', '2', '3', '4', '9']
    print("What do you want? \n"
          "1) Create folder \n"
          "2) Upload file to disk \n"
          "3) Download file \n"
          "4) Get information \n"
          "Choose number")
    choose = input()
    if choose not in options:
        print("No such answer")

    if application == "Yandex":

        if choose == '1':
            print("Name folder?")
            name_folder = input()
            cr.create_folder_yandex(url, headers, name_folder)

        if choose == '2':
            print("Path to download file?\n", r"Example: D:\Cloud")
            folder = input()
            print("Path to download file?\n", r"Example: text.txt")
            file_name = input()
            print("File name on disk?\n", r"Example: hello/text.txt")
            name_file_disk = input()
            print("Replace file on disk if it already exists? yes or no.")
            replace = input()
            uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)

        if choose == '3':
            print("Download file name?\n")
            name_file = input()
            print("Path to download file?\n", r"Example: D:\Cloud")
            directory = input()
            df.download_file_yandex(url, headers, name_file, directory)

        if choose == '4':
            print("Output all data? yes or no")
            output_all_data = input()
            if output_all_data == 'yes':
                name_folder = ''
                gi.get_information_yandex(url, headers, output_all_data, name_folder)
            elif output_all_data == 'no':
                print("What folder or files do you want to find?")
                name_folder = input()
                gi.get_information_yandex(url, headers, output_all_data, name_folder)
            else:
                print("Error! Yes or no!!!")

    if application == "Dropbox":

        if choose == '1':
            print("Only english letters!")
            print("Name folder?")
            name_folder = input()
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            cr.create_folder_dropbox(url, headers, name_folder)

        if choose == '2':
            print("Path to download file?\n", r"Example: D:\Cloud")
            folder = input()
            print("Path to download file?\n", r"Example: text.txt")
            file_name = input()
            print("File name on disk? Only english letters!\n", r"Example: home/text.txt")
            name_file_disk = input()
            uf.upload_file_dropbox(token, folder, file_name, name_file_disk)

        if choose == '3':
            print("Download file name?\n", r"Example: tt.txt")
            name_file = input()
            print("Path to download file?\n", r"Example: D:\Cloud")
            directory = input()
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            }
            df.download_file_dropbox(url, headers, name_file, directory)

        if choose == '4':
            headers = {
                'Authorization': f'Bearer {token}'
            }
            gi.get_information_dropbox(url, headers)
