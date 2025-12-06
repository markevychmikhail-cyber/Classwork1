from alphabet import EngAlphabet

def main():
    """
    Демонстрація роботи класу EngAlphabet.
    """
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    print(EngAlphabet.example())

if __name__ == "__main__":
    main()