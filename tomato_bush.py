from tomato import Tomato

class TomatoBush:
    """
    Клас, що моделює кущ із помідорами.
    """
    def __init__(self, num_tomatoes):
        """
        Створює кущ з заданою кількістю помідорів.

        :param num_tomatoes: кількість помідорів на кущі (int)
        """
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        """
        Змушує дозрівати всі помідори на кущі.
        """
        for tomato in self.tomatoes:
            tomato.grow()

    def show_all_states(self):
        """
        Виводить стан усіх помідорів на кущі.
        """
        for tomato in self.tomatoes:
            tomato.show_state()

    def all_are_ripe(self):
        """
        Перевіряє, чи всі помідори стиглі.

        :return: True, якщо всі стиглі
        """
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        """
        Збирає врожай (очищує список помідорів).
        """
        self.tomatoes = []