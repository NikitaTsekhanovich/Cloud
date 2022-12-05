import requests


def create_folder_yandex(url, headers, name_folder):
    request = requests.put(f'{url}?path={name_folder}', headers=headers)

    if 200 <= request.status_code <= 299:
        print("Folder created!")
        return request
    if request.status_code == 400:
        print("Empty folder name!")
        return request
    if request.status_code == 409:
        print("Folder already created!")
    return request


def create_folder_dropbox(url, headers, name_folder):
    alphabet_and_numbers = list('abcdefghijklmnopqrstuvwxyz1234567890')
    for letter in name_folder.lower():
        if letter not in alphabet_and_numbers:
            print("Only english letters!")
            return "Only english letters!"
    if name_folder == "":
        print("Name is empty!")
        return "Name is empty!"

    data = '{"autorename": false, "path": "/home/' + f'{name_folder}"' + '}'
    request = requests.post(f'{url}files/create_folder_v2', headers=headers, data=data)

    if 200 <= request.status_code <= 299:
        print("Folder created!")
        return request
    if request.status_code == 409:
        print("Folder already created!")
        return request
    return request
