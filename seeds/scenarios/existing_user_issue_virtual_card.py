from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя,
    который загружает свои счета и выполняет выпуск виртуальной карты.
    Создаём 300 пользователей, каждому из которых открываем 1 дебетовый счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счёта.
        Мы создаём 300 пользователей, каждый получит один дебетовый счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300, debit_card_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_issue_virtual_card"


if __name__ == "__main__":
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
