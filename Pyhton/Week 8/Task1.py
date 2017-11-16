class Fraction:
    def __init__(self, numerator, denominator):
       self.num = int(numerator // self.GCD(abs(numerator), abs(denominator)))
       self.denom = int(denominator // self.GCD(abs(numerator), abs(denominator)))

    def GCD(self, numerator, denominator):
        d = 0
        if denominator == 0:
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

def GCD(numerator, denominator):
    d = 0
    if denominator == 0:
        raise ZeroDivisionError
    if denominator < 0:
        denominator = abs(denominator)
        numerator = -1 * numerator
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
    return g, d

result = GCD(2, 2)
print(f"{result}")

f1 = Fraction(48, 18)
print(f"{f1}")
