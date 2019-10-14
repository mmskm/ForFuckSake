class TwoNumbers() :
    def __init__(self, a , b):
        self.number_1 = a
        self.number_2 = b
    def Multiply(self) :
        print(self.number_1, ' * ',self.number_2, ' = ',self.number_1*self.number_2)    
    def Plus(self) :
        print(self.number_1, ' + ',self.number_2, ' = ',self.number_1+self.number_2)   
    def Minus(self) :
        print(self.number_1, ' - ',self.number_2, ' = ',self.number_1-self.number_2)           
    def Divide(self) :
        print(self.number_1, ' / ',self.number_2, ' = ',self.number_1/self.number_2)   



Two_numbers = TwoNumbers(10,5)

Two_numbers.Multiply()
Two_numbers.Minus()
Two_numbers.Plus()
Two_numbers.Divide()