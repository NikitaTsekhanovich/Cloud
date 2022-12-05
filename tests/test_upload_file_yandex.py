import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
import upload_file as uf
import requests


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        folder = "D:\Cloud"
        file_name = "text.txt"
        name_file_disk = "tt.txt"
        replace = "yes"

        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response.status_code, 201)
        requests.delete(f'{url}?path={name_file_disk}&permanently=true', headers=headers)

    def test_wrong_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        folder = "C:\Cgfhhdrtd"
        file_name = "text.txt"
        name_file_disk = "tt.txt"
        replace = "yes"

        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response, "Not found file")

    def test_wrong_file(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        folder = "D:\Cloud"
        file_name = "t.txt"
        name_file_disk = "tt.txt"
        replace = "yes"

        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response, "Not found file")

    def test_name_file_disk(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        folder = "D:\Cloud"
        file_name = "text.txt"
        name_file_disk = "12sf_ sd фыа @#"
        replace = "yes"

        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response.status_code, 201)
        requests.delete(f'{url}?path={name_file_disk}&permanently=true', headers=headers)


    def test_empty_name_file_disk(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        folder = "D:\Cloud"
        file_name = "text.txt"
        name_file_disk = ""
        replace = "yes"

        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response, "Empty name file disk or wrong replace!")

    def test_wrong_replace(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        folder = "D:\Cloud"
        file_name = "text.txt"
        name_file_disk = "txxx.txt"
        replace = "fff"

        uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        response = uf.upload_file_yandex(url, headers, folder, file_name, name_file_disk, replace)
        self.assertEqual(response, "Empty name file disk or wrong replace!")
        requests.delete(f'{url}?path={name_file_disk}&permanently=true', headers=headers)


if __name__ == '__main__':
    unittest.main()
