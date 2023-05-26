import nox
from nox_poetry import session

nox.options.sessions = ["format", "lint"]


@session(python="3.10", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "src", *session.posargs)


@session(python="3.10", reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8", "src")
