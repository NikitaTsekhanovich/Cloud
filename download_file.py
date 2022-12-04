import requests
import urllib.request
import re
import os
import get_information as gi
import found_file as ff


def download_file_yandex(url, headers, name_file, directory):
    try:
        print(*os.scandir(directory))
        found_directory = True
    except FileNotFoundError:
        found_directory = False

    file_found_disk = False
    list_files_disk = gi.get_information_yandex(url, headers, 'no', name_file)
    file_found_disk = get_file_disk(name_file, list_files_disk, file_found_disk)
    print(file_found_disk)
    if found_directory and file_found_disk:
        response = requests.get(f'{url}/download?path={name_file}', headers=headers)
        string = str(response.content)
        link = re.search(r'https://[a-z].+[=v2]', string)
        urllib.request.urlretrieve(link.group(), f"{directory}\{name_file}.zip")

        verified_file = ff.found_file(f'{name_file}.zip', directory)
        if verified_file == f'{name_file}.zip':
            print("Excellent!")
            return "Excellent!"
        else:
            print("Error!")
            return "Error!"
    elif not file_found_disk and found_directory:
        print("File in disk not found!")
        return "File in disk not found!"
    else:
        print("Folder not found!")
        return "Folder not found!"


def download_file_dropbox(url, headers, name_file, directory):
    try:
        print(*os.scandir(directory))
        found_directory = True
    except FileNotFoundError:
        found_directory = False

    if found_directory:
        data = '{"path": ' \
               f'"/home/{name_file}"' \
               '}'
        response = requests.post(f'{url}files/get_temporary_link', headers=headers, data=data)
        if response.status_code == 409:
            print("File in cloud not found!")
            return "File in cloud not found!"
        string = response.text
        link = re.search(r'https://[a-z].+[file]', string)
        urllib.request.urlretrieve(link.group(), f"{directory}\{name_file}")

        verified_file = ff.found_file(f'{name_file}', directory)
        if verified_file == f'{name_file}':
            print("Excellent!")
            return "Excellent!"
        else:
            print("Error!")
            return "Error!"
    elif found_directory:
        print("File in disk not found!")
        return "File in disk not found!"
    else:
        print("Folder not found!")
        return "Folder not found!"


def get_file_disk(name_file, list_files_disk, file_found):
    if len(list_files_disk) != 0:
        for file in range(len(list_files_disk)):
            if list_files_disk[file][8:-1] == name_file:
                file_found = True
    return file_found
