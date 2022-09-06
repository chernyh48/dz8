import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def upload(self, file_path: str, replace=False):
        with open(file_path, "r", encoding='utf-8') as f:
            links = f.read().split('\n')
            for i in links:
                res = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                   params={"path": f"{os.path.basename(i)}",
                                           "overwrite": replace}, headers=self.headers)
                with open(i, "rb") as fl:
                    try:
                        requests.put(res.json()['href'], files={'file': fl})
                    except KeyError:
                        print(res)


if __name__ == '__main__':
    # Файлы загружаются по путям из файла file_list.txt
    path_to_file = "file_list.txt"
    ya_token = "y0_AgAAAAAni3ryAADLWwAAAADODpXp3s8LPyLPShqswfhDbIX0QmTyBJs"
    uploader = YaUploader(ya_token)
    uploader.upload(path_to_file)
