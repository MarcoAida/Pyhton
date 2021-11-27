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
                my_list.append(elements[1])
            
            if elements [1] != 'Sales':
                my_list2.append(element[0])
              
        return(my_list)
        return(my_list2)

shampooFile = CSVFile('shampoo_sales.txt')
shampoo = shampooFile.get_data()

print(shampoo)