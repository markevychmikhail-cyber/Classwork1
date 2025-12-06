class Soda:
    """
    Клас для визначення типу газованої води з можливістю вказати добавку.
    """

    def __init__(self, additive=None):
        """
        Ініціалізація Soda.

        :param additive: добавка до лимонаду (str або None)
        """
        if isinstance(additive, str) and additive.strip():
            self.additive = additive.strip()
        else:
            self.additive = None

    def show_my_drink(self):
        """
        Вивести тип газованої води залежно від наявності добавки.

        :return: None
        """
        if self.additive:
            print(f"Газована вода та {self.additive}")
        else:
            print("Звичайна газована вода")