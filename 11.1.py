#1
class Coins:
    def __init__(self, nominal: int, count: int):
        self.nominal = nominal
        self.count = count

    def info(self) -> str:
        return f"Номинал монеты: {self.nominal}, Количество монет: {self.count}"

    def total_sum(self) -> int:
        return self.nominal * self.count

if __name__ == "__main__":
    print("Задание 1")
    nom = int(input("Введите номинал монеты: "))
    cnt = int(input("Введите количество монет: "))

    coins = Coins(nom, cnt)
    print(coins.info())
    print(f"Общая сумма монет: {coins.total_sum()}")

#2
class Date:
    # Конструктор по умолчанию и конструктор с параметрами (через значения по умолчанию)
    def __init__(self, day: int = 1, month: int = 1, year: int = 2026):
        self.day = day
        self.month = month
        self.year = year

    def __del__(self):
        print(f"[Деструктор] Объект даты ({self.day:02d}.{self.month:02d}.{self.year}) уничтожен.")

    @staticmethod
    def _is_leap(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def _days_in_month(self, month: int, year: int) -> int:
        days = [31, 29 if self._is_leap(year) else 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        return days[month - 1]

    def increase_year(self):
        self.year += 1
        if self.month == 2 and self.day == 29 and not self._is_leap(self.year):
            self.day = 28

    def decrease_by_2_days(self):
        self.day -= 2
        while self.day <= 0:
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1
            self.day += self._days_in_month(self.month, self.year)

    def info(self) -> str:
        return f"Дата: {self.day:02d}.{self.month:02d}.{self.year}"

if __name__ == "__main__":
    print("Задание 2")
    d_default = Date()
    print("По умолчанию:", d_default.info())
    d_const = Date(1, 3, 2026)
    print("Константа:", d_const.info())
    d_const.decrease_by_2_days()
    print("После уменьшения на 2 дня:", d_const.info())
    d = int(input("Введите день: "))
    m = int(input("Введите месяц: "))
    y = int(input("Введите год: "))
    d_user = Date(d, m, y)
    print("Введённая дата:", d_user.info())
    d_user.increase_year()
    print("После увеличения года на 1:", d_user.info())
    d_user.decrease_by_2_days()
    print("После уменьшения на 2 дня:", d_user.info())


