class ExamException(Exception):

    pass
    # raise ExamException('Errore, lista valori vuota')

class MovingAverage():
    
    def __init__(self, len ):
        self.len = len

        try:
            self.len = 2

            #moving_average = MovingAverage(self.len)

        except Exception:
            if(self.len == type(float)):
                raise ExamException('Errore, la lunghezza non può essere con la virgola')

            if(self.len == type(str)):
                raise ExamException('Errore, la lunghezza non può essere un carattere')

            if(self.len == 1):
                raise ExamException('Errore, il valore della finestra è troppo basso, ritorna lo stesso valore')
            
            if(self.len == 3):
                raise ExamException('Errore, il valore della finestra è troppo basso, ritorna lo stesso valore')
            
            if(self.len == 4):
                raise ExamException('Errore, il valore della finestra è troppo basso, ritorna lo stesso valore')
    
    def compute(self, mylist):
        self.mylist = mylist
        myavglist = []
        avg = 0

        i = 0
        j = 1

        try:

            for i in range(len(mylist)):
                
                while (i < 3):
                    element = line.split(',')
                    element[i] = element[j].strip()

                    avg = (element[i] + element[j])/2

                    myavglist.append(avg)
                    i = i + 1
                    j = i + 1
                    avg = 0

        except Exception:

            if(mylist == None):
                raise ExamException('Errore, lista valori vuota')

        return myavglist

moving_average = MovingAverage(2)

result = moving_average.compute( [2,4,8,16] )
#result = moving_average.compute( [] )  #prova lista vuota

print(result)