from math import pi

class FiguraGeometrica:

    def area(self):

        return('metodo area non implementato')

    def perimetro(self):

        return('metodo perimetro non implementato')

    def __str__(self):
        return "Figura geometrica generica"

class Cerchio(FiguraGeometrica):

# Constructor
    def __init__(self, r):
        self.r = r

    def area(self):
        return "Area del cerchio = {}".format(pi * self.r**2)

    def perimetro(self):
        return "Perimetro del cerchio = {}".format(2 * pi * self.r)

    def __str__(self):
        return "Cerchio di raggio {}".format(str(self.r))
    
class Quadrato(FiguraGeometrica):

    # Constructor
    def __init__(self, a):
        self.a = a

    def area(self):
        return "Area del quadrato = {}".format(self.a*self.a)

    def perimetro(self):
        return "Perimetro del quadrato = {}".format(self.a*4)

    def __str__(self):
        return "Quadrato di lato {}".format(str(self.a))
    
class Rettangolo(FiguraGeometrica):

    # Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return "Area del rettangolo = {}".format(self.a * self.b)

    def perimetro(self):
        return "Perimetro del rettangolo = {}".format(self.a * 2 + self.b * 2)

    def __str__(self):
        return "Rettangolo con lati {} e {}".format(str(self.a), str(self.b))
