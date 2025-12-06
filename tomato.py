class Tomato:
    """
    Клас, що моделює помідор та його стадії дозрівання.
    """
    # Статичний атрибут
    states = ["absent", "flower", "green_tomato", "red_tomato"]

    def __init__(self, index):
        """
        Ініціалізує помідор з заданим індексом.

        :param index: індекс помідора на кущі (int)
        """
        self._index = index
        self._state = self.states[0]

    def grow(self):
        """
        Переводить помідор на наступну стадію дозрівання.
        """
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        """
        Перевіряє, чи помідор стиглий (остання стадія).

        :return: True, якщо стиглий
        """
        return self._state == self.states[-1]

    def show_state(self):
        """
        Виводить поточний стан помідора.
        """
        print(f"Tomato {self._index} is {self._state}")