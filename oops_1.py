#initiate a class
class employee:
    #special method/magic /dunder method (Constructor)-
    def __init__(self):
        print(id(self))
        print("started executing attributes/data")
        self.id= 1
        self.salary=1000
        self.designation= "SDE"
        print("attributes/data have been initiated")
    
    #creating Func
    def travel(self, destination):
        print("this travel function call manuallly")
        print(f"employee is travelling to {destination}")
        
        
#Creating Object/Instance
sam = employee()
sam.name="sam k"
#print(sam.name) can create attribut from outside class


print(sam.id)
print(id(sam))

#calling a method:
sam.travel("kerala")

a="x"
b="y"
print(a+b)


