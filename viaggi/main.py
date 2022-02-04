class SearchCity():

    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Stato':
                my_list.append(element)
              
        return(my_list)


cityFile = SearchCity('viaggi.txt')
city = cityFile.get_data()

print(city)