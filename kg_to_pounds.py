class KgToPounds:
    """
    Клас для перетворення кілограмів у фунти з використанням властивостей.
    """

    def __init__(self, kg):
        """
        Ініціалізація класу з вказаною кількістю кілограмів.
        
        :param kg: значення в кілограмах (int або float)
        """
        self.kg = kg  # Використовуємо setter для валідації

    @property
    def kg(self):
        """
        Властивість для отримання поточного значення кг.
        """
        return self.__kg

    @kg.setter
    def kg(self, value):
        """
        Властивість для встановлення нового значення кг.
        Дозволяє лише числові значення.
        """
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            raise ValueError("Кілограми задаються лише числами")

    def to_pounds(self):
        """
        Переводить поточне значення кг у фунти.
        
        :return: відповідне значення у фунтах
        """
        return round(self.__kg * 2.205, 2)