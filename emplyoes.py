class employe() :
    def __init__(self,a,s,d,f) :
        self.name = a
        self.age = s
        self.title = d
        self.salary = f
    def get_salary(self) :
        print(self.name,' salary is ',self.salary)
    def get_info(self) :
        print('The name of employe : ',self.name)
        print('The age of employe : ',self.age)
        print('The title of employe : ',self.title)
        print('The salary of employe : ',self.salary)
    


A = []

for i in range(2) :
    a = input('The name of employe : ')
    b = input('The age of employe : ')
    c = input('The title of employe : ')
    d = input('The salary of employe : ')
    A.append(employe(a,b,c,d))
while True :
    X = input('Number of emp : ')
    for index in range(2) :
        if X == A[index].name :
            s = index
    try :
        A[s].get_info()
    except NameError :
        print('Employe not found') 
    




