class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')

        for line in my_file:
            element = line.split(',')

            if element [0] != 'Date':
                my_file.append(element)

            return(element)

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data()

for line in range(40):
    print(shampoo)