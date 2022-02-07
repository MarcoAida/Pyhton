my_data = open('testdata.csv', 'r')
my_list = []

def compute_avg_monthly_difference(time_series, first_year, last_year):

    myavglist = []
    n = 0
    l = 0
    s = 0
    
    for line in my_data:
        
        element = line.split(',')     #passengers  1949-01 element[0]   ,   112 element[1]
        element[1] = element[1].strip()

        elements = line.split('-')    #year   1949 elements[0]   -   01,112 elements[1]

        if element[0] != 'date' and (int(elements[0]) >= first_year and int(elements[0]) <= last_year):
            
            my_list.append(element[1])  #passengers
               
            for i in range(first_year, last_year):
                    
                if int(elements[0]) % 2 == 0:

                    for m in range(0, 11):

                        l = ( int(element[1]) )

                if int(elements[0]) % 2 == 1:
                    
                    for mm in range(0, 11):
                    
                        n = ( int(element[1]) )
                 
            s = (l - n) / 2

            myavglist.append(s)

            #myavglist.append(element[1])
                             
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
                
        return(my_list)


time_series_file = CSVTimeSeriesFile(name = 'testdata.csv')

time_series = time_series_file.get_data()

print(time_series)
#print("{}" .format(compute_avg_monthly_difference(time_series, 1949, 1950)) )
print('\n')

x = compute_avg_monthly_difference(time_series, 1949, 1950)
#y = compute_avg_monthly_difference(time_series, 1953, 1956)
#z = compute_avg_monthly_difference(time_series, 1955, 1958)

print(x)
#print(y)
#print(z)

print('\n')