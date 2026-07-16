import time

from faker import Faker
from faker.providers.python import TEnum


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """

        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Выбирает случайное значение из enum-типа.

        :param value: Enum-класс для генерации значения.
        :return: Случайное значение из перечисления.
        """

        return self.faker.enum(value)

    def email(self):
        """
        Генерирует случайный email.

        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """

        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        """
        Генерирует случайную категорию покупки из предопределённого списка.

        Используется для имитации типов расходов в системах, моделирующих
        пользовательские транзакции или поведение при оплате товаров и услуг.

        :return: Случайная категория (например, 'gas', 'taxi', 'supermarkets' и т.д.).
        """

        return self.faker.random_element(
            # fmt: off
            [
                "alcohol", "air_tickets", "beauty", "books", "cafes", "cinema",
                "clothing", "education", "electricity", "electronics", "fast_food",
                "flowers", "gaming", "gas_stations", "government_services", "groceries",
                "healthcare", "home_goods", "hotels", "internet", "insurance",
                "marketplace", "mobile", "parking", "pets", "pharmacies",
                "public_transport", "restaurants", "subscriptions", "sports",
                "supermarket", "taxi", "tolls", "travel", "utilities", "water"
            ]
        )
        # fmt: on

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """

        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """

        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя.

        :return: Случайное отчество.
        """

        return self.faker.first_name()

    def phone_number(self) -> str:
        """
        Генерирует случайный номер телефона.

        :return: Случайный номер телефона.
        """

        return self.faker.phone_number()

    def random_float(self, start: int = 1, end: int = 100) -> float:
        """
        Генерирует случайное число с плавающей запятой в указанном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное число с плавающей запятой.
        """

        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Генерирует случайную денежную сумму.

        :return: Сумма от 1 до 1000.
        """

        return self.random_float(end=50000)


fake = Fake(faker=Faker())
