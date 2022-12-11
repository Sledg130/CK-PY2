import doctest

class Car:
    def __init__(self, capacity_tank: [int, float], amount_gasoline: [int, float], speed_car: [int, float], amount_passengers: [int, float]):
        """
        Создание и подготовка к работе объекта "Машина"
        :param capacity_tank: Объем бензобака машины в литрах
        :param amount_gasoline: Количество бензина в баке
        :param speed_car: Скорость машины в м/с
        :param amount_passengers: Количество пассажиров
        Примеры:
        >>> car1 = Car(55, 10, 60, 3)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_tank, (int, float)):
            raise TypeError("Объем бензобака машины должен быть типа int или float")
        if capacity_tank <= 0:
            raise ValueError("Объем бензобака машины должен быть положительным числом")
        self.capacity_tank = capacity_tank

        if not isinstance(amount_gasoline, (int, float)):
            raise TypeError("Количество бензина в баке должно быть типа int или float")
        if amount_gasoline < 0:
            raise ValueError("Количество бензина в баке не должено быть отрицательным числом")
        self.amount_gasoline = amount_gasoline

        if not isinstance(speed_car, (int, float)):
            raise TypeError("Скорость машины должна быть int или float")
        if speed_car < 0:
            raise ValueError("Скорость машины не может быть отрицательным числом")
        self.speed_car = speed_car

        if not isinstance(amount_passengers, (int, float)):
            raise TypeError("Количество пассажиров должно быть int или float")
        if amount_passengers < 0 or amount_passengers > 4:
            raise ValueError("Количество пассажиров не может быть отрицательным числом и больше 4")
        self.amount_passengers = amount_passengers


    def is_empty_tank(self) -> bool:
        """
        Функция, показывающая, пустой ли сейчас бензобак
        :return: Бензобак является пустым
        Примеры:
        >>> car1 = Car(55, 0, 60, 3)
        >>> car1.is_empty_tank()
        """
        ...

    def add_gasoline(self, gasoline: [int, float]) -> None:
        """
        Добавление бензина в бак.
        :param gasoline: Объем добавляемого бензина
        :raise ValueError: Если количество добавляемого бензина превышает свободное место в баке, то вызываем ошибку
        Примеры:
        >>> car1 = Car(55, 10, 60, 3)
        >>> car1.add_gasoline(38)
        """
        if not isinstance(gasoline, (int, float)):
            raise TypeError("Добавляемый бензин должен быть типа int или float")
        if gasoline < 0:
            raise ValueError("Добавляемый бензин должен быть положительным числом")
        ...

    def change_speed(self, speed_car: [int, float], change_speed: [int, float]) -> None:
        """
        Изменение скорости машины.
        :param change_speed: Изменение скорости
        :raise ValueError: Если значение скорости опускается ниже 0, или максимального значения,
        то возвращается ошибка.
        :return: Скорость машины
        Примеры:
        >>> car1 = Car(55, 10, 60, 3)
        >>> car1.change_speed(60, -10)
        """
        max_speed = 240
        if not isinstance(change_speed, (int, float)):
            raise TypeError("Изменяемая скорость должна быть типа int или float")
        if speed_car > max_speed or speed_car <= 0:
            raise ValueError("Скорость должна быть не меньше 0 и не больше максимального значения допустимой скорости")
        ...


class OnlineWallet:
    def __init__(self, accounts_number: [int, float], total_balance: [int, float], dollar_balance: [int, float], credit_account: [int, float]):
        """
        Создание и подготовка к работе объекта "Онлайн кошелёк"
        :param accounts_number: Количество счетов в кошельке
        :param total_balance: Общий счёт в рублях
        :param dollar_balance: Иностранный счёт
        :param credit_account: Депозит кредитного счёта в рублях
        Примеры:
        >>> wallet1 = OnlineWallet(2, 85683, 320, 100000)  # инициализация экземпляра класса
        """
        if not isinstance(accounts_number, (int, float)):
            raise TypeError("Количество счетов должно быть типа int или float")
        if accounts_number < 0:
            raise ValueError("Количество счетов должно быть не отрицательным числом")
        self.accounts_number = accounts_number

        if not isinstance(total_balance, (int, float)):
            raise TypeError("Общий счёт должен быть типа int или float")
        if total_balance < 0:
            raise ValueError("Общий счёт должен быть не отрицательным числом")
        self.total_balance = total_balance

        if not isinstance(dollar_balance, (int, float)):
            raise TypeError("Счёт в долларах должен быть типа int или float")
        if dollar_balance < 0:
            raise ValueError("Иностранный счёт должен быть не отрицательным числом")
        self.dollar_balance = dollar_balance

        if not isinstance(credit_account, (int, float)):
            raise TypeError("Депозит кредитного счёта должен быть типа int или float")
        if credit_account < 0:
            raise ValueError("Депозит кредитного счёта должен быть не отрицательным числом")
        self.credit_account = credit_account

    def is_credit_debt(self) -> bool:
        """
        Функция, показывающая, есть ли задолженность по кредитному счёту
        :return: Есть ли задолженность
        Примеры:
        >>> wallet1 = OnlineWallet(2, 85683, 320, 100000)
        >>> wallet1.is_credit_debt()
        """
        ...

    def add_account(self, new_accounts: [int, float]) -> None:
        """
        Создание нового счёта.
        :param new_accounts: Количество создаваемых счетов
        :return: Действующее количество счетов
        Примеры:
        >>> wallet1 = OnlineWallet(2, 85683, 320, 100000)
        >>> wallet1.add_account(1)
        """
        if not isinstance(new_accounts, (int, float)):
            raise TypeError("Добавляемый счёт должен быть типа int или float")
        if new_accounts < 0:
            raise ValueError("Добавляемый счет не должен быть отрицательным числом")
        ...

    def currency_transfer(self, transfer_amount: [int, float], currency_exchange: [int, float]) -> None:
        """
        Перевод суммы на иностранный счёт.
        :param transfer_amount: Сумма перевода
        :param currency_exchange: Курс перевода
        :raise ValueError: Если сумма перевода меньше общего баланса, то возвращается ошибка.
        :return: Балансы счетов
        Примеры:
        >>> wallet1 = OnlineWallet(2, 85683, 320, 100000)
        >>> wallet1.currency_transfer(25032, 68)
        """
        if not isinstance(transfer_amount, (int, float)):
            raise TypeError("Сумма перевода должна быть типа int или float")
        if transfer_amount <= 0 and transfer_amount > self.total_balance:
            raise ValueError("Сумма перевода должна быть положительным числом и не больше общего баланса")
        if not isinstance(currency_exchange, (int, float)):
            raise TypeError("Курс перевода должен быть типа int или float")
        if currency_exchange <= 0:
            raise ValueError("Курс перевода должен быть положительным числом")
        ...



class NuclearReactor:
    def __init__(self, reactor_power: [int, float], fuel_systems: [int, float]):
        """
        Создание и подготовка к работе объекта "Ядерный реактор"
        :param reactor_power: Мощность реактора
        :param fuel_systems: Количество тепловыделяющих систем
        Примеры:
        >>> Reactor1 = NuclearReactor(1000, 151)  # инициализация экземпляра класса
        """
        if not isinstance(reactor_power, (int, float)):
            raise TypeError("Мощность реактора должна быть типа int или float")
        if reactor_power < 0:
            raise ValueError("Мощность реактора должна быть не отрицательным числом")
        self.reactor_power = reactor_power

        if not isinstance(fuel_systems, (int, float)):
            raise TypeError("Количество тепловыделяющих систем должно быть int или float")
        if fuel_systems < 0:
            raise ValueError("Количество тепловыделяющих систем не может быть отрицательным числом")
        self.fuel_systems = fuel_systems

    def is_reactor_condition(self) -> bool:
        """
        Функция, показывающая, в каком состоянии реактор (при мощности равной нулю реакторв в состоянии Останов, иначе - в рабочем)
        :return: Реактор в рабочем состоянии
        Примеры:
        >>> Reactor1 = NuclearReactor(1000, 151)
        >>> Reactor1.is_reactor_condition()
        """
        ...

    def change_system(self, number_system: [int, float]) -> None:
        """
        Смена отработавшей ТВС на новую.
        :param number_system: Порядковый номер системы
        :raise ValueError: Если порядковый номер ТВС больше общего количества ТВС, равен нулю, или имеет отрицательное значение, то вызывается ошибка)
        Примеры:
        >>> Reactor1 = NuclearReactor(1000, 151)
        >>> Reactor1.change_system(23)
        """
        if not isinstance(number_system, (int, float)):
            raise TypeError("Порядковый номер системы должен быть типа int или float")
        if number_system <= 0 or number_system > self.fuel_systems:
            raise ValueError("Порядковый номер должен быть больше нуля и меньше общего количества ТВС ")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass