import json


class ServerProperties:
    def __init__(self, seed: int, server_ip: str, server_port: int, gamemode: str or int, force_gamemode: bool,
                 online_mode: bool, motd: str, max_player: int):
        self.seed = seed
        self.server_ip = server_ip
        self.server_port = server_port
        self.gamemode = gamemode
        self.force_gamemode = force_gamemode
        self.online_mode = online_mode
        self.motd = motd
        self.max_player = max_player

    def generate(self):
        return f"""level-seed={self.seed}
server-ip={self.server_ip}
rcon.port={self.server_port}
query.port={self.server_port}
server-port={self.server_port}
gamemode={self.gamemode}
force-gamemode={self.force_gamemode.real}
online_mode={self.online_mode.real}
motd={self.motd}
max-player={self.max_player}"""


class Generator:
    # noinspection PyPep8Naming
    def __init__(self, serverName: str, gameVersion: str, config: ServerProperties or None, server_type: str):
        self.serverName = serverName
        self.gameVersion = gameVersion.lower()
        self.server_type = server_type.lower()

        self.config: ServerProperties = config

        if self.server_type == 'mohist':
            if not (self.gameVersion == '1.16.5' or self.gameVersion == '1.12.2'):
                raise Exception('当服务端类型为 mohist 时，只能使用 1.16.5 或 1.12.2 两个版本')

        # 拼接下载地址
        self.gameVersion.replace('.', '_')
        self.server_key = f'mohist_{gameVersion}'

    def generate(self):
        return json.dumps(
            {
                'serverName': self.serverName,
                'gameVersion': self.gameVersion,
                'server_key': self.server_key,
                'config': self.config.generate()
            },
            indent=4
        )
