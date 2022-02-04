class ExamException(Exception):

    pass
    # raise ExamException('Errore, lista valori vuota')

class MovingAverage():
    
    def __init__(self, window):
        if not isinstance(window, int):
            raise ExamException('Invalid type for window, only int supported. Got "{}"'.format(type(window)))

        if window < 1:
            raise ExamException('Negative or zero window value provided')

        self.window = window
        
    def compute(self, mylist):
        self.mylist = mylist
        myavglist = []

        for i in range(len(mylist)+1):
            
            if i < self.window:
                continue
            else:
                myavglist.append(sum(mylist[i - self.window:i])/self.window) 
        return myavglist

class Diff():
                # (ratio e' come se fosse il divisore)
    def __init__(self, ratio, window):
        if not isinstance(window, int):
            raise ExamException('Invalid type for window, only int supported. Got "{}"'.format(type(window)))

        if window < 1:
            raise ExamException('Negative or zero window value provided')

        self.window = window

        if not isinstance(ratio, int):
            raise ExamException('Invalid type for ratio, only int supported. Got "{}"'.format(type(ratio)))

        if ratio < 1:
            raise ExamException('Negative or zero ratio value provided')

        self.ratio = ratio

    def compute(self, mylist):
        self.mylist = mylist
        mydifflist = []

        for i in range(len(mylist)+1):
                
            if i < self.window:
                continue
            else:   # sistemare !! mydifflist.append !!
                mydifflist.append( (sum(mylist[i - self.window:i]) ) - mylist[i-1] )
        
        return mydifflist

moving_average = MovingAverage(2)
result = moving_average.compute( [2,4,8,16] )

#result1 = moving_average.compute( [] )  prova lista vuota

diff = Diff(1,2)
resultD = diff.compute( [2,4,8,16] )
#resultD = diff.compute( [3,7,13,27] )

print(result)

#print(result1)

print(resultD)