import requests
import found_file as ff
import os
import split_file as sf
import zipfile
import create_folder as cf
import re


def upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace):

    if replace == "yes":
        replace = True
    else:
        replace = False

    verified_file = ff.found_file(file_name, folder)

    if verified_file == file_name:

        file_size = os.stat(f'{folder}\{file_name}').st_size
        if file_size / (1024 * 1024 * 1024) < 1:

            with open(f'{folder}\{file_name}', 'rb') as f:
                try:
                    request = requests.get(f'{url}/upload?path={name_file_disk}&overwrite={replace}',
                                           headers=headers).json()
                    response = requests.put(request['href'], files={'file': f})
                    return response
                except KeyError:
                    return "Empty name file disk or wrong replace!"
        else:
            print("File is created...")
            name_without_extension = re.search(r'.+\.', file_name).group()[:-1]
            file_name_zip = zipfile.ZipFile(f'{folder}\{name_without_extension}.zip', 'w')
            file_name_zip.write(f'{folder}\{file_name}')
            number_of_files = sf.split_file(file_name_zip.filename)
            file_name_zip.close()
            os.remove(f"{folder}\{name_without_extension}.zip")
            cf.create_folder_yandex(url, headers, name_without_extension)
            print("Files created")
            print(f'Number of files: {number_of_files}')
            print("loading...")
            for number in range(1, number_of_files + 1):
                file_in_disk = '{}.zip.{}'.format(name_without_extension, str(number).zfill(3))
                file_to_upload = ff.found_file(file_in_disk, folder)
                with open(f'{folder}\{file_to_upload}', 'rb') as f:
                    try:
                        request = requests.get(f'{url}/upload?path={name_without_extension}/{file_in_disk}&overwrite='
                                               f'{replace}', headers=headers).json()
                        requests.put(request['href'], files={'file': f})
                    except KeyError:
                        return "Empty name file disk or wrong replace!"
                os.remove(f'{folder}\{file_to_upload}')

    elif verified_file is None:
        print("Not found file")
        return "Not found file"
    else:
        print("Not found folder")
        return "Not found folder"


def upload_file_dropbox(token, folder, file_name, name_file_disk):
    alphabet_and_numbers = list('abcdefghijklmnopqrstuvwxyz1234567890')
    for letter in name_file_disk.lower():
        if letter not in alphabet_and_numbers and letter != "/" and letter != ".":
            print("Only english letters!")
            return "Only english letters!"
    if name_file_disk == "":
        print("Name is empty!")
        return "Name is empty!"

    verified_file = ff.found_file(file_name, folder)

    if verified_file == file_name:

        file_size = os.stat(f'{folder}\{file_name}').st_size
        if file_size / (1024 * 1024 * 1024) < 1:

            with open(f'{folder}\{file_name}', 'rb') as data:
                try:
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Dropbox-API-Arg': '{"autorename": false, '
                                           '"mode": "add", '
                                           '"mute": false, '
                                           f'"path": "/{name_file_disk}", '
                                           '"strict_conflict": false}',
                        'Content-Type': 'application/octet-stream'
                    }

                    response = requests.post('https://content.dropboxapi.com/2/files/upload', headers=headers, data=data)
                    return response
                except KeyError:
                    return "Empty name file disk!"

        else:
            print("File is created...")
            name_without_extension = re.search(r'.+\.', file_name).group()[:-1]
            file_name_zip = zipfile.ZipFile(f'{folder}\{name_without_extension}.zip', 'w')
            file_name_zip.write(f'{folder}\{file_name}')
            number_of_files = sf.split_file(file_name_zip.filename)
            file_name_zip.close()
            os.remove(f"{folder}\{name_without_extension}.zip")
            print("Files created")
            print(f'Number of files: {number_of_files}')
            print("loading...")
            for number in range(1, number_of_files + 1):
                file_in_disk = '{}.zip.{}'.format(name_without_extension, str(number).zfill(3))
                file_to_upload = ff.found_file(file_in_disk, folder)
                with open(f'{folder}\{file_to_upload}', 'rb') as data:
                    try:
                        headers = {
                            'Authorization': f'Bearer {token}',
                            'Dropbox-API-Arg': '{"autorename": false, '
                                               '"mode": "add", '
                                               '"mute": false, '
                                               f'"path": "/{name_without_extension}/{file_in_disk}", '
                                               '"strict_conflict": false}',
                            'Content-Type': 'application/octet-stream'
                        }
                        requests.post('https://content.dropboxapi.com/2/files/upload',
                                      headers=headers, data=data)
                    except KeyError:
                        return "Empty name file disk or wrong replace!"
                os.remove(f'{folder}\{file_to_upload}')

    elif verified_file is None:
        print("Not found file")
        return "Not found file"
    else:
        print("Not found folder")
        return "Not found folder"
