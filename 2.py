# self refers to the instance of the class

# 1
class Employee:
    company='google'
    def getSalary(self):
        print('salary is',self.salary)
nikhs=Employee()
nikhs.salary=100000
nikhs.getSalary()


# 2
class RailwayForm:
    formType='railway form'
    def printdata(self):
        print(self.name)
        print(self.train)

nikhsapplication=RailwayForm()
nikhsapplication.name='Nikhitha'
nikhsapplication.train='Shatabdi express'
nikhsapplication.printdata()