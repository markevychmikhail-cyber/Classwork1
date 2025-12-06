class TriangleChecker:
    """
    Клас для перевірки можливості утворити трикутник із трьох позитивних відрізків.
    """

    def __init__(self, sides):
        """
        Ініціалізація TriangleChecker.

        :param sides: список або кортеж із трьох чисел (відрізків)
        """
        self.sides = sides

    def is_triangle(self):
        """
        Перевіряє, чи можна з відрізків побудувати трикутник.

        :return: Рядок з результатом перевірки
        """
        # Перевірка типу і довжини
        if not isinstance(self.sides, (list, tuple)) or len(self.sides) != 3:
            return "Потрібно ввести рівно три відрізки!"
        # Перевірка: всі числа та всі більші за 0
        for s in self.sides:
            if not isinstance(s, (int, float)):
                return "Із від'ємними числами нічого не вийде!"
            if s <= 0:
                return "Із від'ємними числами нічого не вийде!"
        a, b, c = self.sides
        # Перевірка умови існування трикутника
        if (a + b > c) and (a + c > b) and (b + c > a):
            return "Ура, можна побудувати трикутник!"
        else:
            return "На жаль, з цього трикутник не зробити."