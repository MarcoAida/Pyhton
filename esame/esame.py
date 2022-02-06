class ExamException(Exception):
   
    #raise ExamException('Errore, lista valori vuota')

    pass


def compute_avg_monthly_difference(time_series, first_year, last_year):

    myavglist = []

    for i in range(len(time_series)+1):
            
        if i < last_year:
            continue
        else:
            myavglist.append(sum(time_series[(i + 1) - i]) / 2) 
    
    return myavglist


class CSVTimeSeriesFile():

    def __init__(self, name):
    
        self.name = name
    
    def get_data(self):
        
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:

            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'date':

                my_list.append(element)
              
        return(my_list)


time_series_file = CSVTimeSeriesFile(name = 'data.csv')

time_series = time_series_file.get_data()

print(time_series)


print("{}" .format(compute_avg_monthly_difference(time_series, 1950, 1952)) )