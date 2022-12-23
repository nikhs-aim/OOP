#  when a class is defined a template is defined. when that template is filled (object instantiation) it can be submitted.

class Number:         
    def sum(self):
        return self.a + self.b
num=Number()
num.a=13
num.b=34
s=num.sum() 
print(s)  