import unittest
import download_file as df
import os

token = 'sl.BUGb3b2bwjosXHm-0Ff_jac1wNDEiT0mA9d4rl8WXUyesMTGT7EBPQJVrEulmd_hEkC7Vb_t1fwRFMsdyBi6KQ2pktt8PEHnBpHm24k2uhltrmoSXgwjlQXq_vFJoxa8nEUo3JGV49LN'


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        url = "https://api.dropboxapi.com/2/"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        name_file = "tt.txt"
        directory = "C:\Cloud"

        result = df.download_file_dropbox(url, headers, name_file, directory)
        self.assertEqual(result, "Excellent!")
        os.remove(r"C:\Cloud\tt.txt")

    def test_wrong_name(self):
        url = "https://api.dropboxapi.com/2/"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        name_file = "nn.txt"
        directory = "C:\Cloud"

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
