import os

db_hostname = os.getenv("DB_HOSTNAME")
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:postgres@" \
                          f"{db_hostname if db_hostname is not None else 'localhost'}:5432/postgres"
