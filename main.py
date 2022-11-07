import create_folder as cr
import upload_file as uf
import download_file as df
import get_information as gi


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def main():
    while True:
        print()
        options = ['1', '2', '3', '4', '9']
        print("What do you want? \n"
              "1) Create folder \n"
              "2) Upload file to disk \n"
              "3) Download file \n"
              "4) Get information \n"
              "9) Exit the program\n"
              "Choose number")
        choose = input()

        if choose not in options:
            print("No such answer")

        if choose == '1':
            print("Name folder?")
            name_folder = input()
            cr.create_folder(URL, headers, name_folder)

        if choose == '2':
            print("Path to download file?\n", r"Example: C:\Cloud")
            folder = input()
            print("Path to download file?\n", r"Example: text.txt")
            file_name = input()
            print("File name on disk?\n", r"Example: hello/text.txt")
            name_file_disk = input()
            print("Replace file on disk if it already exists? yes or no.")
            replace = input()
            uf.upload_file(URL, headers, folder, file_name, name_file_disk, replace)

        if choose == '3':
            print("Download file name?\n")
            name_file = input()
            print("Path to download file?\n", r"Example: C:\Cloud")
            directory = input()
            df.download_file(URL, headers, name_file, directory)

        if choose == '4':
            print("Output all data? yes or no")
            output_all_data = input()
            if output_all_data == 'yes':
                name_folder = ''
                gi.get_information(URL, headers, output_all_data, name_folder)
            elif output_all_data == 'no':
                print("What folder or files do you want to find?")
                name_folder = input()
                gi.get_information(URL, headers, output_all_data, name_folder)
            else:
                print("Error! Yes or no!!!")

        if choose == '9':
            break


if __name__ == "__main__":
    main()
