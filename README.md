# SQL-Query-to-File

This package provides a script that run an SQL query against an
Oracle database and dump the result to a file. The script will look for
the environment variable `DB_CONNECT_STRING_URL` to provide the
[Database URL](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls) for the source database.
