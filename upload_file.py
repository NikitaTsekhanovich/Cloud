import requests
import found_file as ff


def upload_file(URL, headers, folder, file_name, name_file_disk, replace):

    if replace == "yes":
        replace = True
    else:
        replace = False

    request = requests.get(f'{URL}/upload?path={name_file_disk}&overwrite={replace}', headers=headers).json()

    verified_file = ff.found_file(file_name, folder)
    print(replace)

    if verified_file == file_name:
        with open(f'{folder}\{file_name}', 'rb') as f:
            try:
                response = requests.put(request['href'], files={'file': f})
                return response
            except KeyError:
                return "Empty name file disk or wrong replace!"
    elif verified_file == "Not found file":
        print("Not found file")
        return "Not found file"
    else:
        print("Not found folder")
        return "Not found folder"
