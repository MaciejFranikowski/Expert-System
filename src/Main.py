from classes.ExpertSystem import ExpertSystem

if __name__ == "__main__":
    system = ExpertSystem()
    system.loadData('../data/symptom_severity.csv', '../data/dataset.csv')
    # print(system.diseaseDictionary)
    # print(system.symptomArray)
    print(system.possibleDiseases)
    system.limitDisease('itching')
    print(system.possibleDiseases)