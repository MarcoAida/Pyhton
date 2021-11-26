class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                my_list.append(element)
              
        return(my_list)

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data()

print(shampoo)