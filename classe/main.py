class FiguraGeometrica:

    def area(self):

        return('metodo area non implementato')

    def perimetro(self):

        return('metodo perimetro non implementato')

   def __str__(self):
        return "Figura geometrica generica"

implementare le classi derivate Cerchio, Rettangolo, Quadrato (nel modo che si ritiene piu' opportuno) implementando i metodi area, perimetro e __str__ in modo che il codice si comporti nel seguente modo:

Se eseguite le seguenti istruzioni

from figure import FiguraGeometrica,Cerchio,Quadrato,Rettangolo

listafigure = [FiguraGeometrica(), Cerchio(1.0),Quadrato(1.0),Rettangolo(1.0,2.0)]

for f in listafigure:

    print('-'*20)

    print(f)

    print (f.area())

    print( f.perimetro()) 