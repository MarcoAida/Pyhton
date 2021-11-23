class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')

        for line in my_file:
            elements = line.split(',')
    
            if elements [0] != 'Date':
                my_file.append(elements)

        return my_file

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data()

for name in my_file:
    print(my_file)