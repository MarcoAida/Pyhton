values = []
my_file = open('shampoo_sales.txt', 'r')

def my_fun(values):
    sum = 0;
    for i in range(len(values)):
        sum += values[i]
    return sum

j = 0       #controllo    primi 4

for line in my_file:
    elements = line.split(',')
    
    #controllo    primi 4
    if(j > 3):
        break;

    if elements [0] != 'Date':
        date  = elements [0]
        value = elements [1]

        values.append(float(value))
        j = j + 1         #controllo    primi 4

print("Somma: {}" .format(my_fun(values )))