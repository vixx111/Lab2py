class MobileOperator:
    def __init__(self, name: str, minute_cost: float, coverage_area: float):
        self.name = name
        self.minute_cost = minute_cost
        self.coverage_area = coverage_area

    def quality(self) -> float:
        if self.minute_cost <= 0:
            raise ValueError("Стоимость 1 минуты должна быть больше нуля.")
        return 100 * self.coverage_area / self.minute_cost

    def info(self) -> str:
        return (f"Оператор: {self.name}, "
                f"Стоимость 1 мин: {self.minute_cost}, "
                f"Площадь покрытия: {self.coverage_area}, "
                f"Качество Q: {self.quality():.2f}")

class MobileOperatorWithFee(MobileOperator):
    def __init__(self, name: str, minute_cost: float, coverage_area: float, has_connection_fee: bool):
        super().__init__(name, minute_cost, coverage_area)
        self.has_connection_fee = has_connection_fee  # Поле P

    def quality(self) -> float:
        q = super().quality()
        if self.has_connection_fee:
            return 0.7 * q
        return 1.5 * q

    def info(self) -> str:
        fee_str = "Да" if self.has_connection_fee else "Нет"
        return (f"Оператор: {self.name}, "
                f"Стоимость 1 мин: {self.minute_cost}, "
                f"Площадь покрытия: {self.coverage_area}, "
                f"Плата за соединение (P): {fee_str}, "
                f"Качество Qp: {self.quality():.2f}")

if __name__ == "__main__":
    print("Задание 5")
    name = input("Введите название оператора: ")
    cost = float(input("Введите стоимость 1 минуты разговора: "))
    area = float(input("Введите площадь покрытия: "))
    fee_input = input("Есть ли плата за каждое соединение? (да/нет): ").strip().lower()
    has_fee = fee_input in ("да", "yes", "y", "1", "true")

    op1 = MobileOperator(name, cost, area)
    op2 = MobileOperatorWithFee(name, cost, area, has_fee)

    print("\n", op1.info())
    print("", op2.info())