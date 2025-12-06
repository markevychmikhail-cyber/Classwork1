class CoffeeOrder:
    """
    Клас для моделювання замовлення кави.
    """

    def __init__(self, customer_name, coffee_type, size):
        """
        Ініціалізуємо замовлення.

        :param customer_name: Ім'я замовника (str)
        :param coffee_type: Тип кави (str: 'Espresso', 'Cappuccino', 'Latte')
        :param size: Розмір кави ('S', 'M', 'L')
        """
        self.customer_name = customer_name
        self.coffee_type = coffee_type
        self.size = size

    def calculate_price(self):
        """
        Повертає вартість замовлення.

        :return: float, ціна замовлення
        """
        base_prices = {
            'Espresso': 3.00,
            'Cappuccino': 4.50,
            'Latte': 4.75
        }
        size_prices = {
            'S': 0.0,
            'M': 0.5,
            'L': 1.0
        }

        base = base_prices.get(self.coffee_type, 0)
        extra = size_prices.get(self.size, 0)
        total = base + extra
        return round(total, 2)

    def display_order(self):
        """
        Виводить інформацію про замовлення.
        """
        price = self.calculate_price()
        print(f"Замовлення для {self.customer_name}: {self.size} {self.coffee_type} - {price:.2f} грн.")