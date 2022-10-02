import requests
import wget


def get_server_list(type: str):
    servers = requests.get('http://43.154.213.73:30080/server/list').json()

    try:
        server_versions = servers[type]
    except KeyError:
        raise KeyError('输入一个正确的服务端名称！如：mohist_1_16_5，mohist_1_12_2')

    return server_versions


def download_server(type: str, path):
    servers = requests.get('http://43.154.213.73:30080/server/list').json()

    try:
        server_versions = servers[type]
    except KeyError:
        raise KeyError('输入一个正确的服务端名称！如：mohist_1_16_5，mohist_1_12_2')

    wget.download(server_versions[-1]['mirror'], path)
