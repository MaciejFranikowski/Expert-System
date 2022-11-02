import csv
from multiprocessing.dummy import Array


class ExpertSystem:
	def __init__(self):
		self.symptomArray = []
		self.diseaseDictionary = {}
		self.givenSymptoms = []
		self.possibleDiseases = []

	def loadData(self, symptomPath, diseasePath):
		self.loadSymptoms(symptomPath)
		self.loadDiseases(diseasePath)
		self.possibleDiseases = list(self.diseaseDictionary.keys())

	def loadSymptoms(self, symptomPath):
		with open(symptomPath, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.symptomArray.append(row['Symptom'])

	def loadDiseases(self, diseasePath):
		with open(diseasePath, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.diseaseDictionary[row['Disease']] = []
				for value in row:
					if(value != 'Disease' and row[value] != ''):
						self.diseaseDictionary[row['Disease']].append(row[value])

	def giveSymptom(self, symptom):
		if(symptom in self.symptomArray):
			print('Symptom zaakceptowany')
			self.limitDisease(symptom)
		else:
			print('Podany sympton nie znajduje się w bazie')
	
	def limitDisease(self, symptom):
		for disease in self.diseaseDictionary:
			if((symptom not in self.diseaseDictionary[disease]) and (disease in self.possibleDiseases)):
				self.possibleDiseases.remove(disease)
				# print('Symptom ->', symptom)
				# print('Slownik choroby ->', self.diseaseDictionary[disease])
				# print('Deleted from possible diseases ->', disease)

	
