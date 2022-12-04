import requests
import found_file as ff
import os
import split_file as sf
import zipfile


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
            file_name_zip = zipfile.ZipFile(f'{folder}\data2.zip', 'w')
            file_name_zip.write(f'{folder}\{file_name}')
            print(file_name_zip.filename)
            sf.split_file(file_name_zip.filename)
            file_name_zip.close()
            # через цикл закачиваем в облако файл и сразу удаляем.
            # перед этим создаем папку в облаке с названием файла
            # соответственно надо парсить расширение файла, т е убирать его
            print("aaa")

    elif verified_file is None:
        print("Not found file")
        return "Not found file"
    else:
        print("Not found folder")
        return "Not found folder"


def upload_file_dropbox(token, folder, file_name, name_file_disk):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in name_file_disk:
        if letter not in alphabet and letter != "/" and letter != ".":
            print("Only english letters!")
            return "Only english letters!"
    if name_file_disk == "":
        print("Name is empty!")
        return "Name is empty!"
    headers = {
        'Authorization': f'Bearer {token}',
        'Dropbox-API-Arg': '{"autorename": false, '
                           '"mode": "add", '
                           '"mute": false, '
                           f'"path": "/{name_file_disk}", '
                           '"strict_conflict": false}',
        'Content-Type': 'application/octet-stream'
    }

    verified_file = ff.found_file(file_name, folder)

    if verified_file == file_name:
        with open(f'{folder}\{file_name}', 'rb') as f:
            try:
                data = open(f'{folder}\{file_name}', 'rb')
                response = requests.post('https://content.dropboxapi.com/2/files/upload', headers=headers, data=data)
                return response
            except KeyError:
                return "Empty name file disk or wrong replace!"
    elif verified_file is None:
        print("Not found file")
        return "Not found file"
    else:
        print("Not found folder")
        return "Not found folder"
