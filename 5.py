from student import Student

def main():
    """
    Демонстрація роботи класу Student.
    """
    student = Student("Олександр")
    # Додаємо оцінки
    for grade in [10, 9, 11]:
        student.add_grade("Математика", grade)
    for grade in [8, 10]:
        student.add_grade("Історія", grade)
    for grade in [9, 9, 10]:
        student.add_grade("Фізика", grade)
    
    # Виводимо середню оцінку з математики
    print(student.get_average_grade("Математика"))
    # Виводимо загальну середню оцінку
    print(student.get_overall_average_grade())

if __name__ == "__main__":
    main()