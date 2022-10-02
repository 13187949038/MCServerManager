import json
import multiprocessing
import os.path
import random

import click
import utils
import configure
from downloader import server
from configure import Generator, ServerProperties
from prettytable import *
from downloader.server import download_server

logger = utils.get_logger(__name__)


@click.group(help='MC服务器开服工具')
@click.pass_context
def cli(ctx):
    pass


@cli.group(help='服务器配置文件管理')
@click.pass_context
def config(ctx):
    pass


@cli.group(help='服务器管理')
@click.pass_context
def server(ctx):
    pass


@config.command(help='新建配置文件')
@click.option('--output', '-o', help='输出的配置文件', default='./config.json')
def init(output: str):
    # 服务器信息
    server_name = input('请输入服务器名称：')
    game_version = input('游戏版本：')
    server_type = input('服务器类型（目前只有 mohist）：')

    cfg = Generator(serverName=server_name, gameVersion=game_version, server_type=server_type, config=None)

    # 服务器配置
    default_seed = random.randint(2 ** 20, 2 ** 75)
    seed = input(f'服务器地图种子（默认：{default_seed}）：')

    if not seed:
        seed = default_seed
    else:
        seed = int(seed)

    ip = input('服务器ip（一般为 0.0.0.0）：')
    port = int(input('服务器端口（一般为 25565）：'))
    gamemode = input('服务器游戏模式：')

    if gamemode.isdigit():
        gamemode = int(gamemode)

    force_gamemode = bool(input('强制游戏模式（true：开启  false：关闭）：'))
    online_mode = bool(input('正版验证（true：开启  false：关闭）：'))
    motd = input('服务器注释：')
    max_player = int(input('最大玩家数量：'))

    properties = ServerProperties(
        seed=seed,
        server_ip=ip,
        server_port=port,
        gamemode=gamemode,
        force_gamemode=force_gamemode,
        online_mode=online_mode,
        motd=motd,
        max_player=max_player
    )

    cfg.config = properties

    # 导出
    with open(output, 'w', encoding='utf-8') as f:
        f.write(cfg.generate())

    print('success')


@config.command(help='根据配置文件创建服务器')
@click.option('--file', '-f', help='配置文件', default='./config.json')
def apply(file: str):
    file = os.path.abspath(file)

    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            cfg = json.loads(f.read())

        server_list: list = server.get_server_list(
            cfg['server_key']
        )

        table = PrettyTable()
        table.field_names = ['服务端编号', '游戏版本', '服务端 jar', 'MD5', '生成日期']

        for build in server_list:
            table.add_row([
                server_list.index(build),
                build['version'],
                build['name'],
                build['md5'],
                build['date']
            ])

        print(table)

        number = int(input('请输入服务端版本编号：'))
        server_agent = server_list[number]

        print('选择成功！')
        print('开始部署！')

        print('下载服务端程序中！')
        download_server(server_agent['mirror'], './server.jar')
        print('下载完成！')

        with open('server.properties', 'w', encoding='utf-8') as f:
            f.write(cfg['config'])

        with open('eula.txt', 'w', encoding='utf-8') as f:
            f.write('eula=true')

        print('配置完成！')

        print('服务器部署完成！')
    else:
        raise Exception(
            '没有配置文件，请检查当前目录下有没有 config.json 文件。如果没有，请用 -f 参数指定一个，或者用 mcsm config init 来创建一个')


@server.command(help='开启服务器')
def start():
    utils.start_server()


if __name__ == '__main__':
    cli()
