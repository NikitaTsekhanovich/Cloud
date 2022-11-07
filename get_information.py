import requests
import re


def get_information(URL, headers, output_all_data, name_folder):
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
