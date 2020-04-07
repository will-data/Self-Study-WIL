class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

# Unlike Python 2, I don't need to put addtional input 'object' in class definition!
class Student(Person):
# I want to inherit the parent class, Person, and also add new input scores
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avg = float(sum(self.scores)/len(self.scores))
        if avg >=90:
            return('O')
        elif avg >= 80:
            return('E')
        elif avg >= 70:
            return('A')
        elif avg >= 55:
            return('P')
        elif avg >= 40:
            return('D')
        else:
            return('T')

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())