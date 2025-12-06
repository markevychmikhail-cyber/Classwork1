from gardener import Gardener
from tomato_bush import TomatoBush

def main():
    """
    Демонстрація роботи всієї системи садівника, куща й помідорів.
    """
    Gardener.knowledge_base()
    bush = TomatoBush(3)
    gard = Gardener("Іван", bush)

    gard.work()
    gard.work()
    gard.harvest()
    gard.work()
    gard.harvest()

if __name__ == '__main__':
    main()