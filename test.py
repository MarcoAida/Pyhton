my_data = open('testdata.csv', 'r')

def compute_avg_monthly_difference(time_series, first_year, last_year):

        myavglist = []
        n = len(time_series)  # Number of observations
        my_list = []

        for line in my_data:
            
            element = line.split(',')
            element[1] = element[1].strip()
            elements = line.split('-')
            #elements[1] = elements[1].strip()
            
            if element[0] != 'date' and (int(elements[0]) >= first_year and int(elements[0]) <= last_year):
            
                myavglist.append(element[1])
            
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
            
            if element[0] != 'date':
                
                my_list.append(element)

                #if element[0] < '1950':
                    #my_list.append(element[1])
                
        return(my_list)


time_series_file = CSVTimeSeriesFile(name = 'testdata.csv')

time_series = time_series_file.get_data()

#print(time_series)


print("{}" .format(compute_avg_monthly_difference(time_series, 1950, 1953)) )