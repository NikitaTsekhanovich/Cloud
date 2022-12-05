import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
import requests
import create_folder as cf

token = 'sl.BUZtJQKxKoBo_rj4GAiN8vU_5LJWsK0LvdzHwxSfu8gZKv9p8KHhRD0t8rhbdQVq9svDmPG6aaiq9pkvFFuC4F828J_qSeZOIZkoEwmiyPuSub9x6WYPz3aN0Q6DGqdINd7RLjtu5oC1'


class TestCreateFolderDropbox(unittest.TestCase):
    def test_current_name_dropbox(self):
        url = 'https://api.dropboxapi.com/2/'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        current_name = 'hello'
        response = cf.create_folder_dropbox(url, headers, current_name)
        self.assertEqual(response.status_code, 200)
        data = '{"path" : "/home/hello"}'
        requests.post(f'https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)

    def test_all_symbols_dropbox(self):
        url = 'https://api.dropboxapi.com/2/'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        all_symbols = 'he 23 ,.@ вфы'
        response = cf.create_folder_dropbox(url, headers, all_symbols)
        self.assertEqual(response, "Only english letters!")

    def test_empty_name_dropbox(self):
        url = 'https://api.dropboxapi.com/2/'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        empty_name = ''
        response = cf.create_folder_dropbox(url, headers, empty_name)
        self.assertEqual(response, "Name is empty!")

    def test_same_name_dropbox(self):
        url = 'https://api.dropboxapi.com/2/'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        name = 'folder'
        same_name = 'folder'
        response_name = cf.create_folder_dropbox(url, headers, name)
        response_same_name = cf.create_folder_dropbox(url, headers, same_name)
        self.assertEqual(response_name.status_code, 200)
        self.assertEqual(response_same_name.status_code, 409)
        data = '{"path" : "/home/folder"}'
        requests.post(f'https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)


if __name__ == '__main__':
    unittest.main()
