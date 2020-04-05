import click
from .server_new import run_server
#from ..msg_queue import MessageQueue


@click.group()
def cli():
    pass


@cli.command('run-server')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=8000)
@click.argument('url', default="rabbitmq://127.0.0.1:5672/")
def run_server_cmd(host, port, url):

    run_server(host, port, url)


if __name__ == '__main__':
    cli()