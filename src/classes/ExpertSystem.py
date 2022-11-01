import csv
from multiprocessing.dummy import Array


class ExpertSystem:
	def __init__(self):
		print('constr')

	def loadSymptoms(self, symptomPath):
		with open(symptomPath, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			self.symptomArray = []
			for row in reader:
				self.symptomArray.append(row['Symptom'])

	def loadDiseases(self, diseasePath):
		with open(diseasePath, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			self.diseaseDictionary = {}
			for row in reader:
				self.diseaseDictionary[row['Disease']] = []
				for value in row:
					if(value != 'Disease' and row[value] != ''):
						self.diseaseDictionary[row['Disease']].append(row[value])
			
			

