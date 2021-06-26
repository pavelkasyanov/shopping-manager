import click
import uvicorn
import sys

from app.app import app


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', type=str, default="localhost", help='host', show_default=True)
@click.option('-p', '--port', type=int, default=8000, help='port', show_default=True)
def runserver(host: str, port: int) -> None:
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    cli()
