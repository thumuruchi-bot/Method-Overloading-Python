class Calculator:

    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(10, 5))
print(calc.add(10, 5, 15))
