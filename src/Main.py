from classes.ExpertSystem import ExpertSystem

def printMenu():
    print('1 - Input symptom')
    print('2 - Show diagnosis based on given symptoms')
    print('3 - Show available symptoms')
    print('4 - Quit the system')

def printLongLine():
    print('------------------------------------------------------------------------------------------------')

def switch(action, system):
    if action == "1":
        system.giveSymptom(symptom=input('Input symptom: '))
    elif action == "2":
        results(system)
        exit()
    elif action == "3":
        availableSymptoms(system)
    elif action == "4":
        print('The system has stopped.')
        exit()
    else:
        print("Please choose a valid option")

def availableSymptoms(system):
    symptoms = system.symptomArray
    print("Dataset includes aftermentioned symptoms:")
    print(*symptoms, sep = ", ")

def results(system):
    finalDiseases = system.possibleDiseases
    print("Given symptoms would suggest this disease/diseases:")
    print(*finalDiseases, sep = ", ")

def introMessage():
    printLongLine()
    print('Welcome to an expert system assisting in diagnosis')
    print('Please input symtpoms until you see a diagnosis or you have run out of symptoms')
    printLongLine()

def mainLoop(system):
    while True:
        printMenu()
        action = input("What would you like to do? ")
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

