from kg_to_pounds import KgToPounds

def main():
    """
    Демонстрація роботи класу KgToPounds.
    """
    try:
        kg = float(input("Введіть кількість кілограмів: "))
        converter = KgToPounds(kg)
        print(f"{converter.kg} кг = {converter.to_pounds()} фунтів")
        new_kg = float(input("Введіть нову кількість кілограмів: "))
        converter.kg = new_kg  # використання setter
        print(f"{converter.kg} кг = {converter.to_pounds()} фунтів")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()