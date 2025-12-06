from coffee_order import CoffeeOrder
from coffee_shop import CoffeeShop

def main():
    """
    Демонстрація роботи класів CoffeeShop і CoffeeOrder.
    """
    shop = CoffeeShop("My Coffee Place")
    # Створюємо замовлення
    order1 = CoffeeOrder("Андрій", "Espresso", "S")
    order2 = CoffeeOrder("Марія", "Latte", "L")
    order3 = CoffeeOrder("Олена", "Cappuccino", "M")

    # Додаємо замовлення до кав'ярні
    shop.take_order(order1)
    shop.take_order(order2)
    shop.take_order(order3)

    # Виводимо список замовлень
    shop.list_orders()
    # Виводимо загальний дохід
    shop.total_revenue()

if __name__ == "__main__":
    main()