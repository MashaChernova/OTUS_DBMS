from email.policy import default
from faker import Faker
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

@pytest.fixture
def fake():
    return Faker()

@pytest.fixture
def customer_data(fake):
    return {
        'email': fake.email(),
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'telephone': fake.phone_number()
    }

@pytest.fixture
def test_customer_id(customer_data, connection):
     return connection.create_customer(customer_data)