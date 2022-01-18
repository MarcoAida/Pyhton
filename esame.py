class ExamException(Exception):

    pass
    # raise ExamException('Errore, lista valori vuota')

class Diff():
    
    def __init__(self, ratio):
        self.ratio = ratio

        try:
            self.ratio = 1
        
        except Exception:
            if(self.ratio < 1):
                raise ExamException('Errore, il valore della finestra è troppo basso, ritorna lo stesso valore')

            if(self.ratio == type(float)):
                raise ExamException('Errore, la lunghezza non può essere con la virgola')

            if(self.len == type(str)):
                raise ExamException('Errore, la lunghezza non può essere un carattere')

    def compute(self, mylist):
        self.mylist = mylist
        self.ratio = 1
        
        self.mylist = mylist
        mydifflist = []

        dif = 0
        i = 0

        try:
            
            for item in range(len(mylist)):
                
                element = line.split(',')
                if element [i] != element [i+1]:
                    element1  = element [i]
                    element2 = element [i+1]

                    dif = element2 - element1

                    mydifflist.append(int(dif))
                    dif = 0

                while(i <= (len(mylist))):
                    i = i + 1
        
        except Exception:

            if(mylist == None):
                raise ExamException('Errore, lista valori vuota')

            if(mylist == type(float)):
                raise ExamException('Errore, Non puoi passare un float')
            
            if(mylist == type(str)):
                raise ExamException('Errore, Non puoi passare un float')
            
            if(len(mylist) < 2):
                raise ExamException('Errore, lista troppo corta per il calcolo')

        return mydifflist

class MovingAverage():
    
    def __init__(self, len):
        self.len = len

        try:
            self.len = 2

        except Exception:
            if(self.len == type(float)):
                raise ExamException('Errore, la lunghezza non può essere con la virgola')

            if(self.len == type(str)):
                raise ExamException('Errore, la lunghezza non può essere un carattere')

            if(self.len <= 1):
                raise ExamException('Errore, il valore della finestra è troppo basso, ritorna lo stesso valore')
            
            if(self.len > 2):
                raise ExamException('Errore, il valore della finestra è troppo alto, ritorna lo stesso valore')
            
    def compute(self, mylist):
        self.mylist = mylist
        myavglist = []

        avg = 0
        i = 0

        try:

            for item in range(len(mylist)):
                
                element = line.split(',')
                if element [i] != element [i+1]:
                    element1  = element [i]
                    element2 = element [i+1]

                    avg = (element1 + element2)/2

                    myavglist.append(int(avg))
                    avg = 0

                while(i <= (len(mylist))):
                    i = i + 1

        except Exception:

            if(mylist == None):
                raise ExamException('Errore, lista valori vuota')
            
            if(len(mylist) < 2):
                raise ExamException('Errore, lista troppo corta per il calcolo')

        return myavglist

moving_average = MovingAverage(2)

diff = Diff(2)

result = moving_average.compute( [2,4,8,16] )
#result = moving_average.compute( [] )  #prova lista vuota

resultD = diff.compute( [2,4,8,16] )

print(result)
print(resultD)