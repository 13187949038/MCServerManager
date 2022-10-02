import random

import click
import utils
import configure
from configure import Generator, ServerProperties

logger = utils.get_logger(__name__)


@click.group(help='MC服务器开服工具')
@click.pass_context
def cli(ctx):
    pass


@cli.group(help='服务器配置文件管理')
@click.pass_context
def config(ctx):
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


if __name__ == '__main__':
    cli()
