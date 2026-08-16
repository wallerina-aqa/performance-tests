from seeds.scenario import SeedsScenario
from seeds.schema.plan import (
    SeedsPlan,
    SeedUsersPlan,
    SeedAccountsPlan,
    SeedOperationsPlan,
)


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который загружает список операций
    по своему кредитному счёту и смотрит статистику по операциям.
    Создаём 300 пользователей, каждому из которых открываем кредитный счет,
    затем совершаем 5 операций покупки, 1 операцию пополнения счёта и
                                                           1 операцию снятия наличных.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей, их счета и операций.
        Мы создаём 300 пользователей, каждый получит кредитный счёт, по которому
        будут совершены 5 операций покупки, 1 операция пополнения
                                                           и 1 операция снятия наличных.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                ),
            )
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == "__main__":
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
