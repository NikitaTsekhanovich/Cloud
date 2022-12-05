import select_contract as sc


def main():
    while True:
        print("Select cloud: \n"
              "1) Yandex; \n"
              "2) Dropbox; \n"
              "9) Exit the program. \n")
        select_cloud = input()

        if select_cloud == "1":
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            token = ''
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                       'Authorization': f'OAuth {token}'}
            application = "Yandex"
            sc.select_contracts(url, headers, None, application)

        elif select_cloud == "2":
            url = "https://api.dropboxapi.com/2/"
            token = ""
            headers = ""
            application = "Dropbox"
            sc.select_contracts(url, headers, token, application)

        elif select_cloud == '9':
            break
        else:
            print("Incorrect input!")


if __name__ == "__main__":
    main()
