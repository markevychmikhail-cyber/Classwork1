from tomato_bush import TomatoBush

class Gardener:
    """
    Клас, що моделює садівника, який доглядає за рослиною типу TomatoBush.
    """
    def __init__(self, name, plant):
        """
        Ініціалізує садівника з іменем та рослиною.

        :param name: ім'я садівника (str)
        :param plant: рослина (TomatoBush)
        """
        self.name = name
        self._plant = plant

    def work(self):
        """
        Змушує садівника "працювати": рослина переходить на наступну стадію дозрівання, стан показується.
        """
        print(f"Gardener is working...")
        self._plant.grow_all()
        self._plant.show_all_states()
        print("Gardener finished")

    def harvest(self):
        """
        Садівник намагається зібрати врожай.
        """
        print(f"Gardener is harvesting...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Harvesting is finished")
        else:
            print("Too early! Your plant is green and not ripe.")

    @staticmethod
    def knowledge_base():
        """
        Виводить довідкову інформацію із садівництва.
        """
        print(
            "Harvest time for tomatoes should ideally occur\n"
            "when the fruit is a mature green and\n"
            "then allowed to ripen off the vine.\n"
            "This prevents splitting or bruising\n"
            "and allows for a measure of control over the ripening process."
        )