values = []
my_file = open('sales.txt', 'r')

def my_fun(values):
    sum = 0;
    for i in range(len(values)):
        sum += values[i]
    return sum

for line in my_file:
    elements = line.split(',')
    
    if elements [0] != 'Date':
        date  = elements [0]
        value = elements [1]

        values.append(float(value))
        
        my_fun(values)

print("Somma: {}" .format (my_fun(values)) )

class NumericalCSVFile():

    def __init__(self, name):
        self.name = name
        my_file = open(self.name, 'r')
        
    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                value = element [1]
                my_list.append(element)

        return(my_list)

shampooFile = NumericalCSVFile('sales.txt')
sales = shampooFile.get_data()

print(sales)

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        prev_value = None
        
        if(data != None and lenght > 1): # Logica per la predizione
            for i in l:
                
            prediction = im/n
        return prediction
