class ExamException(Exception):

    pass
    # raise ExamException('Errore, ...')


my_data = open('testdata.csv', 'r')
my_list = []

def compute_avg_monthly_difference(time_series, first_year, last_year):
    
    if not isinstance(time_series, list):
        raise ExamException('Invalid type, only list supported. Got "{}"'.format(type(time_series)))

    if time_series == None:
        raise ExamException('Negative or zero value provided')

    if not isinstance(first_year, str):
        raise ExamException('Invalid type, only string supported. Got "{}"'.format(type(first_year)))

    if first_year == None:
        raise ExamException('Negative or zero value provided')

    if not isinstance(last_year, str):
        raise ExamException('Invalid type, only string supported. Got "{}"'.format(type(last_year)))

    if last_year == None:
        raise ExamException('Negative or zero value provided')

    if last_year < first_year:
        raise ExamException('As number last_year must be bigger than first_year')

    myavglist = []
    n = 0
    l = 0
    s = 0
    diff = (int(last_year) - int(first_year) ) + 1
    #print(diff)
    
    for line in my_data:
        
        element = line.split(',')     #passengers  1949-01 element[0]   ,   112 element[1]
        element[1] = element[1].strip()

        if element[1] == int:
            raise ExamException('Invalid type, only int supported. Got "{}"'.format(type(element[1])))
        
        if element[1] == None:
            raise ExamException('Negative or zero value provided')

        elements = line.split('-')    #year   1949 elements[0]   -   01,112 elements[1]

        if elements[0] == int:
            raise ExamException('Invalid type, only int supported. Got "{}"'.format(type(elements[0])))

        if elements[0] == None:
            raise ExamException('Negative or zero value provided')

        if element[0] != 'date' and ( elements[0] >= first_year and elements[0] <= last_year ):
            
            my_list.append(element[1])  #passengers

            for i in range(0, diff):
                
                if int(elements[0]) % 2 == 0:

                    l = int(element[1])

                if int(elements[0]) % 2 == 1:
                    
                    n = int(element[1])

                s = l - n
            
            myavglist.append(s)

            #myavglist.append(element[1])
          
    return myavglist


class CSVTimeSeriesFile():

    def __init__(self, name):
    
        self.name = name
    
    def get_data(self):
       
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        
        #my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            
            element = line.split(',')
            element[1] = element[1].strip()
            
            if element[0] != 'date':
                
                my_list.append(element)
                
        return(my_list)


time_series_file = CSVTimeSeriesFile(name = 'testdata.csv')

time_series = time_series_file.get_data()

print(time_series)

#print("{}" .format(compute_avg_monthly_difference(time_series, 1949, 1950)) )
print('\n')

x = compute_avg_monthly_difference(time_series, "1949", "1950")
#y = compute_avg_monthly_difference(time_series, "1953", "1956")
#z = compute_avg_monthly_difference(time_series, "1955", "1958")

print(x)
#print(y)
#print(z)

print('\n')