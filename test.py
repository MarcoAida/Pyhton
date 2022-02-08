class ExamException(Exception):

    pass
    # raise ExamException('Errore, ...')


def compute_avg_monthly_difference(time_series, first_year, last_year):
     
    if not isinstance(time_series, list):
        raise ExamException('Invalid type, only list supported. Got "{}"'.format(type(time_series)))

    if time_series == None:
        raise ExamException('Negative or zero value provided')

    if not isinstance(first_year, str):
        #raise ExamException('Invalid type, only string supported. Got "{}"'.format(type(first_year)))
        first_year == '1949'

    if first_year == None:
        #raise ExamException('Negative or zero value provided')
        first_year == '1949'
    
    if int(first_year) < 1949 or int(first_year) > 1959:
        raise ExamException('first_year must be between 1949 and 1959')

    if not isinstance(last_year, str):
        #raise ExamException('Invalid type, only string supported. Got "{}"'.format(type(last_year)))
        last_year == '1951'

    if last_year == None:
        #raise ExamException('Negative or zero value provided')
        last_year == '1951'
    
    if int(last_year) < 1950 or int(last_year) > 1960:
        raise ExamException('first_year must be between 1950 and 1960')

    if last_year <= first_year:
        raise ExamException('As number last_year must be bigger than first_year')


    myavglist = []
    my_data = open('testdata.csv', 'r')
    diff = (int(last_year) - int(first_year) ) + 1
    #print(diff)

    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    y12 = []

    #print("1949: {}" .format(y1))
    #print("1950: {}" .format(y2))
    #print("1951: {}" .format(y3))
    #print("1952: {}" .format(y4))
    #print("1953: {}" .format(y5))
    #print("1954: {}" .format(y6))
    #print("1955: {}" .format(y7))
    #print("1956: {}" .format(y8))
    #print("1957: {}" .format(y9))
    #print("1958: {}" .format(y10))
    #print("1959: {}" .format(y11))
    #print("1960: {}" .format(y12))

    s = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    s10 = 0
    s11 = 0
    
    for line in my_data:

        #passengers  1949-01 element[0]   ,   112 element[1]

        element = line.split(',')     
        element[1] = element[1].strip()

        if element[1] != int:
            #raise ExamException('Invalid type, only int supported. Got "{}"'.format(type(element[1])))
            isinstance(element[1], int)
        
        if element[1] == None:
            #raise ExamException('Negative or zero value provided')
            isinstance(element[1], int)

        #year   1949 elements[0]   -   01,112 elements[1]

        elements = line.split('-') 

        if elements[0] != int:
            #raise ExamException('Invalid type, only int supported. Got "{}"'.format(type(elements[0])))
            isinstance(elements[0], int)

        if elements[0] == None:
            #raise ExamException('Negative or zero value provided')
            isinstance(elements[0], int)

        if element[0] != 'date':
        
            if elements[0] == '1949':
                y1.append(element[1])
            
            if elements[0] == '1950':
                y2.append(element[1])

            if elements[0] == '1951':
                y3.append(element[1])

            if elements[0] == '1952':
                y4.append(element[1])

            if elements[0] == '1953':
                y5.append(element[1])
                
            if elements[0] == '1954':
                y6.append(element[1])
                
            if elements[0] == '1955':
                y7.append(element[1])

            if elements[0] == '1956':
                y8.append(element[1])

            if elements[0] == '1957':
                y9.append(element[1])

            if elements[0] == '1958':
                y10.append(element[1])

            if elements[0] == '1959':
                y11.append(element[1])

            if elements[0] == '1960':
                y12.append(element[1])

        #if elements[0] >= first_year and elements[0] <= last_year:
        
    for i in range(0, 12):
        
        s1 = (int(y2[i]) - int(y1[i]) )     #50-49

        s2 = (int(y3[i]) - int(y2[i]) )     #51-50

        s3 = (int(y4[i]) - int(y3[i]) )     #52-51

        s4 = (int(y5[i]) - int(y4[i]) )     #53-52

        s5 = (int(y6[i]) - int(y5[i]) )     #54-53

        s6 = (int(y7[i]) - int(y6[i]) )     #55-54

        s7 = (int(y8[i]) - int(y7[i]) )     #56-55

        s8 = (int(y9[i]) - int(y8[i]) )     #57-56

        s9 = (int(y10[i]) - int(y9[i]) )    #58-57

        s10 = (int(y11[i]) - int(y10[i]) )    #59-58

        s11 = (int(y12[i]) - int(y11[i]) )    #60-59

        s = ( (s1 + s2) / 2 )

        if ( int(y1[i]) == 0 or int(y2[i]) == 0 or int(y3[i]) == 0 or int(y4[i]) == 0 or int(y5[i]) == 0 or int(y6[i]) == 0 or int(y7[i]) == 0 or int(y8[i]) == 0 or int(y9[i]) == 0 or int(y10[i]) == 0 or int(y11[i]) == 0 or int(y12[i]) == 0 ) and diff < 3:
            i = i + 1
            s = 0

        myavglist.append(s)
        
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
        
        my_list = []

        for line in my_file:
            
            element = line.split(',')
            element[1] = element[1].strip()
            
            if element[0] != 'date':
                
                my_list.append(element)
                
        return(my_list)


time_series_file = CSVTimeSeriesFile(name = 'testdata.csv')

time_series = time_series_file.get_data()

x = compute_avg_monthly_difference(time_series, "1949", "1951")


#print(time_series)

print('\n')

print(x)

print('\n')