# Programming Exercises 1-7 
class Fraction: 

    def __init__(self, num, den):
        # check to make sure  num and den are integer if not, raise an exception
       
        try: 
            # given 2/8, reduce to 1/4 when initialized
            gcd = self.gcd(num, den)
            self.num = int(num/gcd)
            self.den = int(den/gcd)
        except Exception:
            if type(num) != int:
                numtype = type(num)
                print(f"Fraction class only accepts integers for the num, a {numtype} was given")
            if type(den) != int:
                dentype = type(den)
                print(f"Fraction class only accept integers for the den, a {dentype} was given")


    def __repr__(self):
        return f"Fraction class: {self.num} / {self.den}"

    def __str__(self):
        return f"Fraction class: {self.num} / {self.den}"

    def gcd(self,n,m):

        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn

        return n

    def getNum(self):
        return self.num


    def getDen(self):
        return self.den


    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        if newnum == 0:
            return int(newden)

        if newden == 0:
            return 0

        return Fraction(newnum, newden)

        
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)


    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)


    def __gt__(self, other):
        # greater than, return bool
        newnum = self.num * other.den
        othernum = self.den * other.num
        if newnum > othernum:
            return True
        return False


    def __ge__(self, other):
        # greater than or equal, return bool
        newnum = self.num * other.den
        othernum = self.den * other.num
        if newnum >= othernum:
            return True
        return False
        

    def __lt__(self, other):  
        # less than, return bool 
        newnum = self.num * other.den
        othernum = self.den * other.num
        if newnum < othernum:
            return True
        return False


    def __le__(self, other):
        # less than or equal, return bool
        newnum = self.num * other.den
        othernum = self.den * other.num
        if newnum <= othernum:
            return True
        return False


    def __ne__(self, other):
        # not equal, return bool
        newnum = self.num * other.den
        othernum = self.den * other.num
        if newnum != othernum:
            return True
        return False

    def __add__(self, other): 
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        if newnum == 0:
            return int(newden)

        if newden == 0:
            return 0

        return Fraction(newnum, newden)

    
    def __radd__(self, other):
        return Fraction.__add__(self, other)


    


f1 = Fraction(3,4)
f2 = Fraction(1,4)
f3 = f1 - f2
f4 = f1 * f2
f5 = f1 / f2

templist = [3, 2, 5, 5]

newfraction = f1 + Fraction((int(len(templist)/4)), 5)

