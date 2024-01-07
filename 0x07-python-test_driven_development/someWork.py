class Calculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Testing the Calculator class
if __name__ == "__main__":
    calculator = Calculator(10,50)
    
    result = calculator.add()

    if result != 60:
        print("Bad result:", result)
    else:
        print("good work >_<")

cal = Calculator(10, 15)
print(cal.add())  # This will print 25
