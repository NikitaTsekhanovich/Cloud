import requests


def create_folder(URL, headers, name_folder):
    request = requests.put(f'{URL}?path={name_folder}', headers=headers)

    if 200 <= request.status_code <= 299:
        print("Folder created!")
        return request
    if request.status_code == 400:
        print("Empty folder name!")
        return request
    if request.status_code == 409:
        print("Folder already created!")
    return request
