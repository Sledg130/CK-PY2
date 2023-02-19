import random

class Fighter:
    """
    Документация на класс.
    Класс описывает героя Воина.
    """

    def __init__(self, name: str, lvl: int, strength: int, experience_points: int):
        """
        Инициализация экземпляра класса.
        :param name: Имя героя
        :param lvl: Уровень героя
        :param strength: Сила героя
        :param ExperiencePoints: Опыт героя

        Пример:
        >>> fighter1 = Fighter("Джеймс", 1, 16, 0)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(lvl, int):
            raise TypeError("Уровень должен быть типа int")
        if lvl <= 0:
            raise ValueError("Уровень должен быть положительным числом")
        self._lvl = lvl

        if not isinstance(strength, int):
            raise TypeError("Сила должна быть типа int")
        if strength <= 0:
            raise ValueError("Сила должна быть положительным числом")
        self._strength = strength

        if not isinstance(experience_points, int):
            raise TypeError("Опыт должен быть типа int")
        if experience_points < 0:
            raise ValueError("Опыт не может быть отрицательным числом")
        self._experience_points = experience_points

    def __str__(self):
        """
        Метод возвращает строку для чтения.

        Пример:
        >>> fighter1 = Fighter("Джеймс", 1, 16, 0)
        >>> print(fighter1)
        """
        return f"Воин {self.name}; Уровень {self._lvl}; Сила {self._strength}; Опыт {self._experience_points}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.

        Пример:
        >>> fighter1 = Fighter("Джеймс", 1, 16, 0)
        >>> print(repr(fighter1))
        """
        return f"{self.__class__.__name__}(Имя={self.name!r}, Уровень={self._lvl!r}, Сила={self._strength!r}, Опыт={self._experience_points!r})"

    def lvl_up(self):
        """
        Метод определяет уровень героя по имеющемуся опыту. Если опыт достигает определённого уровня, то атрибут lvl меняется.

        Пример:
        >>> fighter1.lvl_up()
        """
        Experience_of_lvl = [0, 300, 900, 2700, 6500, 14400, 23000, 34000, 48000, 64000, 85000, 100000]

        for exp in Experience_of_lvl:
            if self._experience_points < exp:
                self._lvl = Experience_of_lvl.index(exp)
                print("Уровень героя", self._lvl)
                break

        return self._lvl

    def exp_up(self, experience: int):
        """
        Метод увеличивает количество имеющегося опыта.

        Пример:
        >>> fighter1.exp_up(1000)
        """
        self.experience = experience
        self._experience_points += self.experience
        print("Получено опыта", self._experience_points)
        return self._experience_points

    def attack(self):
        """
        Метод позволяет провести атаку по цели. Удар считается успешным, если число на кубике больше 10.

        Пример:
        >>> fighter1.attack()
        """
        hit = random.randint(1, 20)
        print("Бросаем кубик... Выпало:", hit)
        if hit > 10:
            print(True)
        else:
            print(False)

class Knight(Fighter):
    """
    Документация на дочерний класс.
    Класс описывает подкласс героя Воина -- Рыцаря.
    """
    def __init__(self, name: str, lvl: int, strength: int, experience_points: int, inspiration = None):
        """
        Инициализация экземпляра подкласса.
        :param name: Имя героя
        :param lvl: Уровень героя
        :param strength: Сила героя
        :param ExperiencePoints: Опыт героя
        :param Inspiration: Вдохновение. Приравнивается уровню или задаётся вручную.

        Пример:
        >>> knight1 = Knight("Джеймс", 1, 16, 0, 2)
        """
        super().__init__(name, lvl, strength, experience_points)
        if inspiration is None:
            inspiration = self._lvl
        self._inspiration = inspiration

        if not isinstance(inspiration, int):
            raise TypeError("Вдохновение должно быть типа int")
        if inspiration <= 0:
            raise ValueError("Вдохновение должно быть положительным числом")

    def __str__(self):
        """
        Метод возвращает строку для чтения.
        Перегрузку метода реализовали из-за необходимости указания подкласса героя.

        Пример:
        >>> knight1 = Knight("Джеймс", 1, 16, 0, 2)
        >>> print(knight1)
        """
        s_str = super().__str__()
        return f"{s_str}; Вдохновение: {self._inspiration}; Подкласс: {self.__class__.__name__}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        Перегрузку метода реализовали из-за необходимости указания подкласса героя.

        Пример:
        >>> knight1 = Knight("Джеймс", 1, 16, 0, 2)
        >>> print(repr(knight1))
        """
        s_repr = super().__repr__()
        return f"{s_repr}; Вдохновение={self._inspiration!r}; Подкласс={self.__class__.__name__!r}"

    def attack(self):
        """
        Метод позволяет провести атаку по цели. Удар считается успешным, если число на кубике больше 10.
        Перегрузка метода реализовали из-за того, что подкласс Рыцарь имеет возможность провести второй удар.

        Пример:
        >>> knight1.attack()
        """
        s_attack = super().attack()
        hit_2 = random.randint(1, 20)
        print("Будешь проводить ещё один удар?")
        answer = input()
        if answer == "Да":
            print("Бросаем кубик... Выпало:", hit_2)
            if hit_2 > 10:
                print(True)
            else:
                print(False)
        elif answer == "Нет":
            print("Дополнительную атаку не провели")
        else:
            print("Не могу тебя понять")

if __name__ == "__main__":
    fighter1 = Fighter("Джеймс", 1, 16, 0)
    #fighter1.attack()
    knight1 = Knight("Джеймс", 3, 16, 899)
    #knight1.attack()
    pass

