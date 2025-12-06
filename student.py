class Student:
    """
    Клас, що представляє студента з системою оцінок по предметах.
    """

    def __init__(self, name):
        """
        ініціалізує студента з ім'ям та порожнім словником оцінок.

        :param name: Ім'я студента
        """
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        Додає оцінку з певного предмета.

        :param subject: Назва предмета (str)
        :param grade: Оцінка (int або float)
        """
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def get_average_grade(self, subject):
        """
        Повертає середню оцінку з вказаного предмету.
        
        :param subject: Назва предмета
        :return: Середня оцінка (float, округлена до 2 знаків після коми) або 0, якщо предмет відсутній
        """
        grades = self.grades.get(subject, [])
        if not grades:
            return 0
        return round(sum(grades) / len(grades), 2)

    def get_overall_average_grade(self):
        """
        Повертає середню оцінку з усіх предметів.
        
        :return: загальна середня оцінка (float, округлена до 2 знаків після коми) або 0, якщо оцінок немає
        """
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 2)