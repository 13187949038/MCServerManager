import requests
import wget


def get_server_list(type: str):
    servers = requests.get('http://43.154.213.73:30080/server/list').json()

    try:
        server_versions = servers[type]
    except KeyError:
        raise KeyError(f'输入一个正确的服务端名称！如：mohist_1_16_6，mohist_1_12_2  {type}')

    return server_versions


def download_server(url, path):
    wget.download(url, path)
