import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
import create_folder as cf
import requests


class TestCreateFolderYandex(unittest.TestCase):
    def test_current_name_yandex(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        current_name = 'hello'
        response = cf.create_folder_yandex(url, headers, current_name)
        self.assertEqual(response.status_code, 201)
        requests.delete(f'{url}?path={current_name}&permanently=true', headers=headers)

    def test_all_symbols_yandex(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        all_symbols = 'he 23 ,.@ вфы'
        response = cf.create_folder_yandex(url, headers, all_symbols)
        self.assertEqual(response.status_code, 201)
        requests.delete(f'{url}?path={all_symbols}&permanently=true', headers=headers)

    def test_empty_name_yandex(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        empty_name = ''
        response = cf.create_folder_yandex(url, headers, empty_name)
        self.assertEqual(response.status_code, 400)

    def test_same_name_yandex(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = ''
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        name = 'folder'
        same_name = 'folder'
        response_name = cf.create_folder_yandex(url, headers, name)
        response_same_name = cf.create_folder_yandex(url, headers, same_name)
        self.assertEqual(response_name.status_code, 201)
        self.assertEqual(response_same_name.status_code, 409)
        requests.delete(f'{url}?path={name}&permanently=true', headers=headers)


if __name__ == '__main__':
    unittest.main()
