import click
import utils
import configure

logger = utils.get_logger(__name__)


@click.group(help='MC服务器开服工具')
@click.pass_context
def cli(ctx):
    pass


@cli.command()
def test():
    print(configure.Generator('aaa', 'bbb', 'ccc',
                              configure.ServerProperties(123456, '0.0.0.0', 25565, 'creative', True, True, 'test',
                                                         10)).generate())


if __name__ == '__main__':
    cli()
