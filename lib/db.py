import pymysql
import time
from datetime import datetime

def my_decoratot(func):
    try:
        func()
    except Exception as e:
        print(f"Ошибка: {e}")

class DbConnecter():
    def __init__(self, host, port, user, password, database ):
        self.connection = self.connect_to_database(host, port, user, password, database)
        self.cursor = self.connection.cursor()



    def connect_to_database(self, host, port, user, password, database):
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor)
        return connection


    def create_customer(self, customer_data: dict) -> int:

        full_customer_data = {
            'customer_group_id': "1",
            'email': 'mail@mail.ty',
            'password': "unknown",
            'language_id': '1',
            'firstname': "unknown",
            'lastname': "anonim",
            'telephone': "+7",
            'custom_field': "text",
            'ip': "unknown",
            'status': "1",
            'safe': "1",
            'token': "1",
            'code': "1",
            "date_added": "1900-01-01"
        }
        for customer_data_key in list(customer_data):
            full_customer_data[str(customer_data_key)] = str(customer_data.get(customer_data_key))
        try:
            keys = list(full_customer_data)
            keys_str = ', '.join(keys)
            print(keys_str)
        except Exception as e:
            print(f"Ошибка: {e}")
        try:
            values = full_customer_data.values()
            values_str = '"' + '", "'.join(values) + '"'
            print(values_str)
        except Exception as e:
            print(f"Ошибка: {e}")
        try:
            sql = f"INSERT INTO oc_customer ({keys_str}) VALUES ({values_str});"
            print(f" sql {sql}")
            self.cursor.execute(sql)
            id = self.cursor.fetchall()
            print(id)
        except Exception as e:
            raise AssertionError(f"Ошибка: {e}")
        try:
            return self.check_id_for_attribute('email', customer_data.get('email'))
        except Exception as e:
            raise AssertionError(f"Ошибка: {e}")



    def get_tables(self):
        try:
            #cursor = self.connection.cursor()
            self.cursor.execute("SHOW TABLES")
            tables = self.cursor.fetchall()
            for i, table in enumerate(tables, 1):
                # Извлекаем название таблицы (зависит от формата результата)
                table_name = list(table.values())[0] if table else "unknown"
                print(f"{i:3}. {table_name}")
            return tables

        except Exception as e:
            print(f"Ошибка: {e}")


    def check_id_for_attribute(self, key, value):
        try:
            sql = f"SELECT customer_id FROM oc_customer WHERE {key}='{value}'"
            self.cursor.execute(sql)
            id = self.cursor.fetchall()
            print(id)
            return id[0].get('customer_id')
        except LookupError:
            raise LookupError('такого id нет в списке')
        except Exception as e:
            print(f"Ошибка: {e}")

    def get_id_list(self):
        sql = "SELECT customer_id FROM oc_customer"
        try:
            self.cursor.execute(sql)
            ids_dict = self.cursor.fetchall()
        except Exception as e:
            print(f"Ошибка: {e}")
        try:
            ids_list = [id.get('customer_id') for id in ids_dict]
            print(ids_list)
            return ids_list
        except Exception as e:
            print(f"Ошибка: {e}")

    def get_all_custimer_data(self,id):
        try:
            sql = f"SELECT * FROM oc_customer WHERE customer_id={id}"  #WHERE customer_id={id}
            self.cursor.execute(sql)
            id = self.cursor.fetchall()
            print(id[0])
            return id[0]
        except LookupError:
            raise LookupError('такого id не существует')
        except Exception as e:
            print(f"Ошибка: {e}")


    def check_customer_data_for_id(self, id, attribute_name):
        try:
            sql = f"SELECT {attribute_name} FROM oc_customer WHERE customer_id={id}"  #WHERE customer_id={id}
            self.cursor.execute(sql)
            id = self.cursor.fetchall()
        except Exception as e:
            print(f"Ошибка: {e}")
        try:
            print(id)
            return id[0].get(attribute_name)
        except LookupError as e:
            raise LookupError("нет такого элемента")



    def update_customer(self, customer_id, update_dict):
        attribute_list = []
        for key in list(update_dict):
            attribute_list += [f"{key}='{update_dict.get(key)}'"]
        sql = "UPDATE oc_customer SET " + ', '.join(attribute_list) + f" WHERE customer_id={customer_id}"
        print(sql)
        try:
            res = self.cursor.execute(sql)
            print("result = ", res)
        except Exception as e:
            print(f"Ошибка: {e}")
        return res


    def remove_customer(self, customer_id):
        try:
            sql = f"DELETE FROM oc_customer WHERE customer_id={customer_id}"  #WHERE customer_id={id}
            res = self.cursor.execute(sql)
            return res
        except Exception as e:
            print(f"Ошибка: {e}")

conn = DbConnecter('192.168.0.164', 3306, 'bn_opencart', '', 'bitnami_opencart')
conn.create_customer({'email': "111@iu.ff"})
# conn.check_id_for_attribute('email', "2")
# # n=2
# conn.update_customer(n,{'email': '70ii@ii.ii'})
# # print("номер записи: " + str(n))
#conn.check_customer_data_for_id(8, '*')
#print(conn.check_customer_data_for_id(2, ['email']))
#print(conn.get_id_list())
#conn.get_all_custimer_data(2)