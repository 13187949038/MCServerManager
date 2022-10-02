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
max-player={self.max_player}
        """


class Generator:
    # noinspection PyPep8Naming
    def __init__(self, serverName: str, gameVersion: str, server_url: str, config: ServerProperties):
        self.serverName = serverName
        self.gameVersion = gameVersion
        self.server_url = server_url

        self.config: ServerProperties = config

    def generate(self):
        return json.dumps(
            {
                'serverName': self.serverName,
                'gameVersion': self.gameVersion,
                'server_url':  self.server_url,
                'config': self.config.generate()
            }
        )
