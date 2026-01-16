#def password(text):
#    if len(text) > 8:
#        if text.isalnum():
#            print("Password is Valid")
#        else:
#            print("Password is Invalid")
#p = input("Enter a valid password")
#password(p)


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
          return self.a + self.b
    
    def sub(self):
          return self.a - self.b
          
    def mul(self):
          return self.a * self.b
    
    def div(self):
          return self.a / self.b if self.b != 0 else "Error Divide by Zero"
          
a = int(input())
b = int(input())
calc = Calculator(a, b)   

print("Add: ", calc.add())
print("Sub: ", calc.sub())
print("Mul: ", calc.mul())
print("Div: ", calc.div())
    
            
         
           