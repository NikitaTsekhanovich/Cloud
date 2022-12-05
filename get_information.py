import requests
import re


def get_information_yandex(URL, headers, output_all_data, name_folder):
    if output_all_data == 'yes':
        information = requests.get(f'{URL}/files', headers=headers).text
        all_files = re.findall(r'"name":".+?"', information)
        print(all_files)
        return
    elif output_all_data == 'no':
        information = requests.get(f'{URL}?path={name_folder}', headers=headers).text
        all_files = re.findall(r'"name":".+?"', information)
        print(all_files)
        return all_files


def get_information_dropbox(url, headers):
    response = requests.post(f'{url}file_requests/count', headers=headers)
    print(response.text)
