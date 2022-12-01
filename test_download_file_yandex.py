import unittest
import download_file as df
import os


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "hello"
        directory = "C:\Cloud"

        result = df.download_file_yandex(url, headers, name_file, directory)

        self.assertEqual(result, "Excellent!")
        os.remove(f"C:\Cloud\hello.zip")

    def test_wrong_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "he"
        directory = "C:\Cloud"

        result = df.download_file_yandex(url, headers, name_file, directory)
        self.assertEqual(result, "File in disk not found!")

    def test_wrong_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        name_file = "hello"
        directory = "C:\Csdfsdjflksdl"

        result = df.download_file_yandex(url, headers, name_file, directory)
        self.assertEqual(result, "Folder not found!")


if __name__ == '__main__':
    unittest.main()
