from nox_poetry import session


@session(python=["3.10", "3.11", "3.12"])
def test(session):
    args = session.posargs or ["--cov"]
    session.install("pytest", "pytest-cov", ".")
    session.run("pytest", *args)
