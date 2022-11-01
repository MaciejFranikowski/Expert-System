from classes.ExpertSystem import ExpertSystem

if __name__ == "__main__":
    system = ExpertSystem()
    system.loadSymptoms('../data/symptom_severity.csv')
    system.loadDiseases('../data/dataset.csv')