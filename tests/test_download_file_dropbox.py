import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
import download_file as df
import os

token = 'sl.BUZtJQKxKoBo_rj4GAiN8vU_5LJWsK0LvdzHwxSfu8gZKv9p8KHhRD0t8rhbdQVq9svDmPG6aaiq9pkvFFuC4F828J_qSeZOIZkoEwmiyPuSub9x6WYPz3aN0Q6DGqdINd7RLjtu5oC1'


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        url = "https://api.dropboxapi.com/2/"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        name_file = "tt.txt"
        directory = "D:\Cloud"

        result = df.download_file_dropbox(url, headers, name_file, directory)
        self.assertEqual(result, "Excellent!")
        os.remove(r"D:\Cloud\tt.txt")

    def test_wrong_name(self):
        url = "https://api.dropboxapi.com/2/"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        name_file = "nn.txt"
        directory = "D:\Cloud"

        result = df.download_file_dropbox(url, headers, name_file, directory)
        self.assertEqual(result, "File in cloud not found!")

    def test_wrong_folder(self):
        url = "https://api.dropboxapi.com/2/"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        name_file = "tt.txt"
        directory = "C:\Csadfsadfud"

        result = df.download_file_dropbox(url, headers, name_file, directory)
        self.assertEqual(result, "Folder not found!")


if __name__ == '__main__':
    unittest.main()
