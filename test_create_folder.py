import unittest
import create_folder as cf


class TestCreateFolder(unittest.TestCase):
    def test_current_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        current_name = 'hello'
        response = cf.create_folder(url, headers, current_name)
        self.assertEqual(response.status_code, 201)

    def test_all_symbols(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        all_symbols = 'he 23 ,.@ вфы'
        response = cf.create_folder(url, headers, all_symbols)
        self.assertEqual(response.status_code, 201)

    def test_empty_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        empty_name = ''
        response = cf.create_folder(url, headers, empty_name)
        self.assertEqual(response.status_code, 400)

    def test_same_name(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        token = 'y0_AgAAAAAQYR9KAAh4ZgAAAADQfjk_bKIgrybFTXCKscIlG_h7KSCIOoA'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {token}'}
        name = 'folder'
        same_name = 'folder'
        response_name = cf.create_folder(url, headers, name)
        response_same_name = cf.create_folder(url, headers, same_name)
        self.assertEqual(response_name.status_code, 201)
        self.assertEqual(response_same_name.status_code, 409)


if __name__ == '__main__':
    unittest.main()
