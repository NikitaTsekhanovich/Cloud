import unittest
import upload_file as uf
import requests


token = "sl.BUUQ-Dp6QtI7aJvlSK1zr_enZYR1LvKi6VMrHws4Nw9V2j_W5WtdzFoqYri1uFznvlS3TbMN85MFmpwz3esoWGuARSyisPoI3GqwFH59NNMrq4DSajCT0BNCLbo7tIPZGI58gD2MaOaz"
url = 'https://api.dropboxapi.com/2/'


class TestUploadFile(unittest.TestCase):
    def test_current_request(self):
        name_file_disk = "home/text.txt"
        file_name = "text.txt"
        folder = "D:\Cloud"

        response = uf.upload_file_dropbox(url, token, folder, file_name, name_file_disk)
        self.assertEqual(response.status_code, 200)
        data = '{"path" : "/home/text.txt"}'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        requests.post(f'https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)

    def test_wrong_folder(self):
        name_file_disk = "/home/text.txt"
        file_name = "text.txt"
        folder = "C:\Cgfhhdrtd"

        response = uf.upload_file_dropbox(url, token, folder, file_name, name_file_disk)
        self.assertEqual(response, "Not found file")

    def test_wrong_file(self):
        name_file_disk = "/home/text.txt"
        file_name = "tt.txt"
        folder = "D:\Cloud"

        response = uf.upload_file_dropbox(url, token, folder, file_name, name_file_disk)
        self.assertEqual(response, "Not found file")

    def test_name_file_disk(self):
        name_file_disk = "12sf_ sd фыа @#"
        file_name = "text.txt"
        folder = "D:\Cloud"

        response = uf.upload_file_dropbox(url, token, folder, file_name, name_file_disk)
        self.assertEqual(response, "Only english letters!")

    def test_empty_name_file_disk(self):
        name_file_disk = ""
        file_name = "text.txt"
        folder = "D:\Cloud"

        response = uf.upload_file_dropbox(url, token, folder, file_name, name_file_disk)
        self.assertEqual(response, "Name is empty!")


if __name__ == '__main__':
    unittest.main()
