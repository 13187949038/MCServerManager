import click


@click.group(help='MC服务器开服工具')
@click.pass_context
def cli(ctx):
    pass


if __name__ == '__main__':
    cli()
