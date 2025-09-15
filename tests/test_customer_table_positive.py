import pytest

@pytest.mark.only2
def test_create_customer(connection, customer_data):
    customer_id = connection.create_customer(customer_data)
    for key, value in customer_data.items():
        res_value = connection.check_customer_data_for_id(customer_id, key)
        assert res_value == value, f"значения по полю {key} не совпали {res_value} вместо {value}"
    connection.remove_customer(customer_id)

@pytest.mark.only2
def test_update_customer(connection, customer_data, test_customer_id):
    customer_id = test_customer_id
    attributes_for_change = customer_data
    connection.update_customer(customer_id, attributes_for_change)
    for key, value in customer_data.items():
        res_value = connection.check_customer_data_for_id(customer_id, key)
        assert res_value == value, f"значения по полю {key} не совпали {res_value} вместо {value}"


@pytest.mark.only
def test_remove_customer(connection, test_customer_id):
    customer_id = test_customer_id

    connection.remove_customer(customer_id)
    assert customer_id not in connection.get_id_list(), f'значение не удалено {connection.get_id_list()}'

