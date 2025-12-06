class Human:
    """
    Клас, що представляє людину з характеристиками: ім'я, вік, гроші та житло.
    """

    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        """
        Ініціалізація обʼєкта Human.
        :param name: Імʼя людини
        :param age: Вік людини
        """
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        """
        Довідкова інформація про людину.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money:.2f}")
        print(f"House: {self.__house}")

    @staticmethod
    def default_info():
        """
        Вивести стандартні значення для імені та віку.
        """
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def __make_deal(self, house, price):
        """
        Придбати будинок ― зменшити гроші та встановити житло.
        :param house: Обʼєкт будинку
        :param price: Ціна будинку
        """
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        """
        Заробити гроші (збільшити баланс).
        :param amount: Сума грошей
        """
        self.__money += amount
        print(f"Earned {amount} money! Current value: {self.__money:.2f}")

    def buy_house(self, house, discount):
        """
        Купити будинок із знижкою, якщо грошей достатньо.
        :param house: Будинок
        :param discount: Знижка у відсотках (0.0..1.0)
        """
        price = house.final_price(discount)
        print(f"Final price: {price:.2f}")
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money!")

class House:
    """
    Клас, що описує Будинок з площею і ціною.
    """

    def __init__(self, area, price):
        """
        Ініціалізація будинку.
        :param area: Площа
        :param price: Вартість
        """
        self._area = area
        self._price = price

    def final_price(self, discount):
        """
        Ціна будинку з урахуванням знижки.
        :param discount: Знижка у відсотках (0.0..1.0)
        :return: Нова ціна
        """
        return self._price * (1 - discount)

class SmallHouse(House):
    """
    Клас Невеликий Типовий Дім, площа 40м2
    """

    def __init__(self, price):
        """
        Ініціалізація SmallHouse: площа 40м2.
        :param price: Вартість
        """
        super().__init__(40.0, price)

if __name__ == '__main__':
    # Тести згідно завдання

    # Вивід default_info
    Human.default_info()

    # Створення людини
    h = Human("Sasha", 27)
    h.info()

    # Створення будинку
    house = SmallHouse(9500)
    # Купівля будинку зі знижкою 0.15 (тобто 15%)
    discount = 0.15
    h.buy_house(house, discount)
    # Заробіток грошей
    h.earn_money(5000)
    h.buy_house(house, discount)
    h.earn_money(20000)
    h.buy_house(house, discount)
    # Повторний виклик info()
    h.info()