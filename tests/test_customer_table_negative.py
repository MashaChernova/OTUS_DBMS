import pytest
import random

@pytest.mark.only2
def test_update_customer_neg(connection, customer_data):
    attributes_for_change = customer_data
    customer_id = max(connection.get_id_list())+1
    print(customer_id)
    assert not connection.update_customer(customer_id, attributes_for_change)


@pytest.mark.only3
def test_remove_customer_neg(connection):
    customer_id = max(connection.get_id_list()) + random.randint(1, 10)
    assert not connection.remove_customer(customer_id), f'нет информации о выходе за границы диапазона'
