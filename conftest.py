from email.policy import default

import pytest
import logging
from lib.db import DbConnecter

def pytest_addoption(parser):
    parser.addoption("--host", help="Database url", default="192.168.0.164")
    parser.addoption("--port", help="Database port", default=3306)
    parser.addoption("--database", help="database name", default='bitnami_opencart')
    parser.addoption("--user", help="database user name", default="bn_opencart")
    parser.addoption("--password", help="database user password", default="")

@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption('--host')
    port = request.config.getoption('--port')
    database = request.config.getoption('--database')
    user = request.config.getoption('--user')
    password = request.config.getoption('--password')
    connecter = DbConnecter(host, port, user, password, database)
    return connecter
