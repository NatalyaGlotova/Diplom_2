from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'Nataly@test.ru',
        "password": "123456789"}

    data_negative = {
        "email": 'Nataly123@test.ru',
        "password": "password"}

    data_double = {
        "email": 'Nataly@test.ru',
        "password": "123456789",
        "name": "Глотова Наталья"}

    data_without_email = {
        "email": '',
        "password": "123456789",
        "name": "Глотова Наталья"}

    data_without_password = {
        "email": 'Nataly@test.ru',
        "password": "",
        "name": "Глотова Наталья"}

    data_without_name = {
        "email": 'Nataly@test.ru',
        "password": "123456789",
        "name": ""}
