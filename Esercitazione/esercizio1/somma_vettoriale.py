class CSVFile():
    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []
        my_list2 = []

        for line in my_file:
            element = line.split(',')
            element[0] = element[0].strip()

            elements = line.split(',')
            elements[1] = elements[1].strip()
            
            if element [0] != 'Date':
                my_list.append(element [0])

            if elements [0] != 'Date':
                my_list2.append(elements [1])
        
        print('Dimensione lista: {}' .format(len(my_list)) )
        print('Dimensione lista2: {}' .format(len(my_list2)) )

        sum_vett = 0
        my_lis = []

        if( len(my_list) == len(my_list2) ):
            sum_vett = (len(my_list) + len(my_list2))
            print('Somma vettoriale: {}' .format(sum_vett) )
        else :
            print('{}' .format(my_lis) )
        
        print('{}' .format(my_list) )
        return(my_list2)


shampooFile = CSVFile('shampoo_sales.txt')
shampoo = shampooFile.get_data()

print(shampoo)