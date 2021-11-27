class CSVFile():
    
    def __init__(self, name):
        self.name = name
    
    #prima colonna

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            element = line.split(',')
            element[0] = element[0].strip()
            
            if element [0] != 'Date':
                my_list.append(element [0])
            
        return(my_list)
    
    #seconda colonna

    def get_data2(self):
        my_file = open(self.name, 'r')
        my_list2 = []
        
        for line in my_file:
            elements = line.split(',')
            elements[1] = elements[1].strip()
            
            if elements [0] != 'Date':
                my_list2.append(elements [1])
        
        return(my_list2)

shampooFile = CSVFile('shampoo_sales.txt')
shampoo = shampooFile.get_data()
shampoo2 = shampooFile.get_data2()

print(shampoo)
print(shampoo2)