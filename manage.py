import subprocess

import click
import uvicorn

from app.app import app  # noqa: ignore


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
@click.option(
    "-d",
    "--debug",
    type=bool,
    default=False,
    help="debug mode",
    show_default=True,
)
@click.option(
    "-r",
    "--reload",
    type=bool,
    default=False,
    help="reload after update",
    show_default=True,
)
def runserver(host: str, port: int, debug: bool, reload: bool) -> None:
    uvicorn.run(
        "manage:app",
        host=host,
        port=port,
        debug=debug,
        workers=1,
        reload=reload,
    )


@cli.command(help="apply migration")
def migrate() -> int:
    return subprocess.call(["alembic", "upgrade", "head"])  # nosec


@cli.command(help="Make migration")
@click.option("-m", "--msg", help="Add a message")
def migration(msg: str) -> int:
    return subprocess.call(["alembic", "revision", "-m", f"{msg}"])  # nosec


if __name__ == "__main__":
    cli()
