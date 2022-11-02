from classes.ExpertSystem import ExpertSystem

def printMenu():
    print('1 - Podaj symptom')
    print('2 - Wyświetl wynik na podstawie podanych symptomów')
    print('3 - Zakończ działanie programu')

def printLongLine():
    print('------------------------------------------------------------------------------------------------')

def switch(action, system):
    if action == "1":
        system.giveSymptom(symptom=input('Podaj symptom: '))
    elif action == "2":
        results(system)
        exit()
    elif action == "3":
        print('Koniec pracy systemu')
        exit()
    else:
        print("Proszę wybierz poprawną opcję")

def results(system):
    finalDiseases = system.possibleDiseases
    print("Podane symptomy wskazują na choroby/chorobę:")
    print(*finalDiseases, sep = ", ")

def introMessage():
    printLongLine()
    print('Witaj w systemie eksperckim wspomagającym diagnozę choroby')
    print('Podawaj symptomy do momentu podania przez system diagnozy lub kiedy zakończysz podawać symptomy')
    printLongLine()

def mainLoop(system):
    while True:
        printMenu()
        action = input("Co chciałbyś zrobić?    ")
        switch(action, system)
        printLongLine()
        if(len(system.possibleDiseases) == 1):
            results(system)
            exit()
            

if __name__ == "__main__":
    system = ExpertSystem()
    system.loadData('/Users/maciej/Git/Expert_System/data/symptom_severity.csv', '/Users/maciej/Git/Expert_System/data/dataset.csv')
    introMessage()
    mainLoop(system)

