import random

class Fighter:
    """
    Документация на класс.
    Класс описывает героя Воина.
    """

    def __init__(self, name: str, lvl: int, strength: int, ExperiencePoints: int):
        """
        Инициализация экземпляра класса.
        :param name: Имя героя
        :param lvl: Уровень героя
        :param strength: Сила героя
        :param ExperiencePoints: Опыт героя
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(lvl, int):
            raise TypeError("Уровень должен быть типа int")
        if lvl <= 0:
            raise ValueError("Уровень должен быть положительным числом")
        self.lvl = lvl

        if not isinstance(strength, int):
            raise TypeError("Сила должна быть типа int")
        if strength <= 0:
            raise ValueError("Сила должна быть положительным числом")
        self.strength = strength

        if not isinstance(ExperiencePoints, int):
            raise TypeError("Опыт должен быть типа int")
        if ExperiencePoints < 0:
            raise ValueError("Опыт не может быть отрицательным числом")
        self.ExperiencePoints = ExperiencePoints

    def __str__(self):
        """
        Метод возвращает строку для чтения.
        """
        return f"Воин {self.name}; Уровень {self.lvl}; Сила {self.strength}; Опыт {self.ExperiencePoints}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        """
        return f"{self.__class__.__name__}(Имя={self.name!r}, Уровень={self.lvl!r}, Сила={self.strength!r}, Опыт={self.ExperiencePoints!r})"

    def lvl_up(self):
        """
        Метод определяет уровень героя по имеющемуся опыту.
        """
        Experience_of_lvl = [0, 300, 900, 2700, 6500, 14400, 23000, 34000, 48000, 64000, 85000, 100000]
        for exp in Experience_of_lvl:
            if self.ExperiencePoints < exp:
                self.lvl = Experience_of_lvl.index(exp)
                print("Уровень героя", self.lvl)
                break
        return self.lvl

    def exp_up(self, Experience: int):
        """
        Метод увеличивает количество имеющегося опыта.
        """
        self.Experience = Experience
        self.ExperiencePoints += self.Experience
        print("Получено опыта", self.ExperiencePoints)
        return self.ExperiencePoints

    def attack(self):
        """
        Метод позволяет провести атаку по цели. Удар считается успешным, если число на кубике больше 10.
        """
        hit = random.randint(1, 20)
        print("Бросаем кубик... Выпало:", hit)
        if hit > 10:
            print("Попадание")
        else:
            print("Промах")

class Knight(Fighter):
    """
    Документация на дочерний класс.
    Класс описывает подкласс героя Воина -- Рыцаря.
    """
    def __init__(self, name: str, lvl: int, strength: int, ExperiencePoints: int, Inspiration = None):
        """
        Инициализация экземпляра подкласса.
        :param name: Имя героя
        :param lvl: Уровень героя
        :param strength: Сила героя
        :param ExperiencePoints: Опыт героя
        :param Inspiration: Вдохновение. Приравнивается уровню или задаётся вручную.
        """
        super().__init__(name, lvl, strength, ExperiencePoints)
        if Inspiration is None:
            Inspiration = self.lvl
        self.Inspiration = Inspiration

        if not isinstance(Inspiration, int):
            raise TypeError("Вдохновение должно быть типа int")
        if Inspiration <= 0:
            raise ValueError("Вдохновение должно быть положительным числом")

    def __str__(self):
        """
        Метод возвращает строку для чтения.
        Перегрузку метода реализовали из-за необходимости указания подкласса героя.
        """
        s_str = super().__str__()
        return f"{s_str}; Подкласс: {self.__class__.__name__}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        Перегрузку метода реализовали из-за необходимости указания подкласса героя.
        """
        s_repr = super().__repr__()
        return f"{s_repr}; Подкласс={self.__class__.__name__!r}"

    def attack(self):
        """
        Метод позволяет провести атаку по цели. Удар считается успешным, если число на кубике больше 10.
        Перегрузка метода реализовали из-за того, что подкласс Рыцарь имеет возможность провести второй удар.
        """
        s_attack = super().attack()
        hit_2 = random.randint(1, 20)
        print("Будешь проводить ещё один удар?")
        answer = input()
        if answer == "Да":
            print("Бросаем кубик... Выпало:", hit_2)
            if hit_2 > 10:
                print("Попадание")
            else:
                print("Промах")
        elif answer == "Нет":
            print("Дополнительную атаку не провели")
        else:
            print("Не могу тебя понять")

if __name__ == "__main__":
    Fighter = Fighter("Джеймс", 1, 16, 0)
    #Fighter.lvl_up()
    #Fighter.exp_up(1000)
    Knight = Knight("Джеймс", 3, 16, 899)
    #Knight.attack()
    pass

