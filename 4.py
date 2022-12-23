'''
instance attribute: An attribute that belongs to the
                    instance (object).

The preference is given to the instance attribute
over the class attribute.
'''


class Employee:
    company='Google'         # specific to each class
    salary=100               # second preference (if the instance attribute was not present, this will be printed )

nikhs=Employee()             
rin=Employee()
nikhs.salary=300             # instance attribute (first preference)
Employee.company='yt'        # changing cass attribute
print(nikhs.company)
print(rin.company)
print(nikhs.salary)