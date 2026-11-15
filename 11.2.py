class Coins:
    def __init__(self, nominal: float, count: int):
        self.nominal = nominal
        self.count = count

    def info(self) -> str:
        return f"Номинал монеты: {self.nominal} грн, Количество: {self.count}"

    def total_sum(self) -> float:
        return self.nominal * self.count

class CoinsCurrency(Coins):
    def __init__(self, nominal: float, count: int, usd_rate: float):
        super().__init__(nominal, count)
        self.usd_rate = usd_rate

    def cost_in_cents(self) -> float:
        if self.usd_rate <= 0:
            raise ValueError("Курс доллара должен быть больше нуля.")
        return (self.total_sum() / self.usd_rate) * 100

    def info(self) -> str:
        return (f"{super().info()}, Курс $: {self.usd_rate} грн, "
                f"Сумма: {self.total_sum():.2f} грн ({self.cost_in_cents():.2f} центов)")

if __name__ == "__main__":
    print("Задание 3")
    nom = float(input("Введите номинал монеты в грн: "))
    cnt = int(input("Введите количество монет: "))
    rate = float(input("Введите стоимость 1$ в гривне: "))

    parent_obj = Coins(nom, cnt)
    child_obj = CoinsCurrency(nom, cnt, rate)

    print(parent_obj.info(), f"| Сумма: {parent_obj.total_sum():.2f} грн")
    print(child_obj.info())



#2
import datetime
class Date:
    def __init__(self, day: int = 1, month: int = 1, year: int = 2026):
        self.day = day
        self.month = month
        self.year = year
    def info(self) -> str:
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

class Employee(Date):
    def __init__(self, fio: str, day: int, month: int, year: int):
        super().__init__(day, month, year)
        self.fio = fio

    def years_of_service(self, current_date: datetime.date = None) -> int:
        if current_date is None:
            current_date = datetime.date.today()

        years = current_date.year - self.year
        if (current_date.month, current_date.day) < (self.month, self.day):
            years -= 1
        return max(0, years)

    def info(self) -> str:
        return (f"Работник: {self.fio}, "
                f"Дата поступления: {super().info()}, "
                f"Стаж: {self.years_of_service()}")


if __name__ == "__main__":
    print(" Задание 4")
    d = int(input("Введите день:"))
    m = int(input("Введите месяц:"))
    y = int(input("Введите год:"))
    fio = input("Введите ФИО работника:")

    date_obj = Date(d, m, y)
    emp_obj = Employee(fio, d, m, y)

    print("\nКласс-родитель (Дата):", date_obj.info())
    print("Класс-потомок (Работник):", emp_obj.info())