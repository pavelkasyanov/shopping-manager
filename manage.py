import subprocess

import click
import uvicorn

from app.app import app


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-h",
    "--host",
    type=str,
    default="localhost",
    help="host",
    show_default=True,
)
@click.option(
    "-p", "--port", type=int, default=8000, help="port", show_default=True
)
def runserver(host: str, port: int) -> None:
    uvicorn.run(app, host=host, port=port)


@cli.command(help="apply migration")
def migrate() -> int:
    return subprocess.call(["alembic", "upgrade", "head"])  # nosec


@cli.command(help="Make migration")
@click.option("-m", "--msg", help="Add a message")
def migration(msg: str) -> int:
    return subprocess.call(["alembic", "revision", "-m", f"{msg}"])  # nosec


if __name__ == "__main__":
    cli()
