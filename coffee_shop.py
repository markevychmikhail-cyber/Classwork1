from coffee_order import CoffeeOrder

class CoffeeShop:
    """
    Клас кав'ярні.
    """

    def __init__(self, name):
        """
        Ініціалізує кав'ярню.

        :param name: Назва кав'ярні (str)
        """
        self.name = name
        self.orders = []

    def take_order(self, order):
        """
        Додає замовлення до списку кав'ярні.

        :param order: Об'єкт CoffeeOrder
        """
        if isinstance(order, CoffeeOrder):
            self.orders.append(order)

    def list_orders(self):
        """
        Виводить всі наявні замовлення.
        """
        print(f"Список замовлень у {self.name}:")
        for order in self.orders:
            order.display_order()

    def total_revenue(self):
        """
        Обчислює та виводить загальний дохід.
        """
        total = sum(order.calculate_price() for order in self.orders)
        print(f"Загальний дохід: {total:.2f} грн.")