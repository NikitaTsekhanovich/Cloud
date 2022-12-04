import unittest
import download_file as df
import os

token = 'sl.BURocvw96mnfisG88VDGqJi8km4bA4ZCZDuCaLR5i89f-rLGGC6WzyJtBOIbqCF9AYPyWP2v5XAdbb5OK0qUe40Ml4N_ACuKb_hmj7_YzGpdKqdLdw2ozl4i7v2HFdSwTP5QrIMhqfcX'


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
