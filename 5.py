'''
The constant part can be passed as a parameter, here sign is thanks and there will be no change
but salary changes. Therefore it is made as an attribute. 

@staticmethod - it is used when you need a function that does not access any properties off a class.
                To say functions inside the static method is not dependent on class.

'''


class Employee:
    company='google'
    def getSalary(self,sign):
        print(f'salary is {self.salary}\n{sign}')

    @staticmethod      
    def greet():
        print('good morninng!')
        
nikhs=Employee()
nikhs.greet()       # put Employee.greet() and check for static method - no error, because no self
nikhs.salary=100000
nikhs.getSalary("thanks!")    # put Employee.getSalary("thanks!") and check for static method - error, because self is created and it is dependent on the object nikhs.
