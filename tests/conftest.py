import pytest
from sqlalchemy import create_engine


@pytest.fixture(scope="function")
def engine():
    registry_db_dsn = "postgresql://user:content@127.0.0.1:6543/test_db"
    return create_engine(registry_db_dsn, connect_args={"connect_timeout": 10}, pool_recycle=1800)