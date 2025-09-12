import pytest
from faker import Faker
import random

@pytest.mark.only2
def test_create_customer(connection):
    fake = Faker()
    email = fake.email()
    attribute_for_customer = {'email': email, 'firstname': fake.first_name()}
    customer_id = connection.create_customer(attribute_for_customer)
    assert connection.check_customer_data_for_id(customer_id, 'email') == email, 'значения не совпали'

@pytest.mark.only2
def test_update_customer(connection):
    fake = Faker()
    attributes_for_change = {'firstname': fake.first_name() , 'lastname': fake.last_name() , 'email': fake.email(), 'telephone': fake.phone_number()}
    attributes_key = list(attributes_for_change)
    customer_id = random.choice(connection.get_id_list())
    connection.update_customer(customer_id, attributes_for_change)
    result_date = [connection.check_customer_data_for_id(customer_id, attribute_for_change) for attribute_for_change in attributes_key]
    assert result_date == list(attributes_for_change.values()), f"{result_date} вместо {list(attributes_for_change.values())} "

@pytest.mark.only
def test_remove_customer(connection):
    customer_id = random.choice(connection.get_id_list())
    customers_info = connection.get_all_custimer_data(customer_id)
    customers_info.pop('customer_id')
    customers_info.pop('date_added')
    print(customers_info)
    connection.remove_customer(customer_id)
    assert customer_id not in connection.get_id_list(), f'значение не удалено {connection.get_id_list()}'
    try:
        connection.create_customer(customers_info)
    except:
        raise AssertionError('исследование не добавлено после удаления')
