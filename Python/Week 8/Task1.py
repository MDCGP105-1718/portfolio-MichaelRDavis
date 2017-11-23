# A fraction class for perfoming calculations on fractions
class Fraction:
    # Init fraction class, find the GCD of both the denominator and numerator
    def __init__(self, numerator, denominator):
       self.num = int(numerator // self.GCD(abs(numerator), abs(denominator)))
       self.denom = int(denominator // self.GCD(abs(numerator), abs(denominator)))

    # Find the greatest common divisor
    def GCD(self, numerator, denominator):
        d = 0
        if denominator < 0:
            denominator = abs(denominator)
            numerator = -1 * numerator
        elif denominator == 0:
            raise ZeroDivisionError
        while numerator % 2 == 0 and denominator % 2 == 0:
            numerator = numerator // 2
            denominator = denominator // 2
            d = d + 1
        while numerator != denominator:
            if numerator % 2 == 0:
                numerator = numerator // 2
            elif denominator % 2 == 0:
                denominator = denominator // 2
            elif numerator > denominator:
                numerator = (numerator - denominator) // 2
            else:
                denominator = (denominator - numerator) // 2
        g = numerator
        return g

    def Add(self, other):
        return self.num * other.denom + self.denom * other.num, self.denom * other.denom

    def Subtract(self, other):
        return self.num * other.denom - self.denom * other.num, self.denom * other.denom

    def Multiply(self, other):
        return self.num * other.num , self.denom * other.denom

    def Divide(self, other):
        return self.num * other.denom, self.denom * other.num

    def Inverse(self, other):
       return

# Begin algorithm test for finding the greatest common divisor
def GCD(numerator, denominator):
    d = 0
    if denominator < 0:
        denominator = abs(denominator)
        numerator = -1 * numerator
    elif denominator == 0:
        raise ZeroDivisionError
    while numerator % 2 == 0 and denominator % 2 == 0:
        numerator = numerator // 2
        denominator = denominator // 2
        d = d + 1
    while numerator != denominator:
        if numerator % 2 == 0:
            numerator = numerator // 2
        elif denominator % 2 == 0:
            denominator = denominator // 2
        elif numerator > denominator:
            numerator = (numerator - denominator) // 2
        else:
            denominator = (denominator - numerator) // 2
    g = numerator
    return g

result = GCD(48, 18)
print(f"{result}")
# End algorithm test for finding the greatest common divisor

f1 = Fraction(3, 4)
f2 = Fraction(3, 4)
f3 = Fraction.Add(f1, f2)
print(f"{f3}")
f4 = Fraction.Subtract(f1, f2)
print(f"{f4}")
f5 = Fraction.Multiply(f1, f2)
print(f"{f5}")
f6 = Fraction.Divide(f1, f2)
print(f"{f6}")
