'''
class attribute: An attribute that belongs to the class
                  rather than a particuar object.
'''

class Employee:
    company='Google'         # specific to each class

nikhs=Employee()             # object instantiation
rin=Employee()
## (changing class attribute)
rin.company='yt'             # to change a particular person's company 
# Employee.company='yt'      # to change all company name
print(nikhs.company)
print(rin.company)