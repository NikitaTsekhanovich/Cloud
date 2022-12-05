import sys
import os
import requests
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import create_folder as cf
import unittest
import download_file as df
import os


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "hello"
        cf.create_folder_yandex(url, headers, name_file)
        directory = "D:\Cloud"

        result = df.download_file_yandex(url, headers, name_file, directory)

        self.assertEqual(result, "Excellent!")
        requests.delete(f'{url}?path={name_file}&permanently=true', headers=headers)
        os.remove(f"D:\Cloud\hello.zip")

    def test_wrong_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "he"
        directory = "D:\Cloud"

        result = df.download_file_yandex(url, headers, name_file, directory)
        self.assertEqual(result, "File in disk not found!")

    def test_wrong_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "hello"
        directory = "C:\Csdfsdjflksdl"

        result = df.download_file_yandex(url, headers, name_file, directory)
        self.assertEqual(result, "Folder not found!")


if __name__ == '__main__':
    unittest.main()
