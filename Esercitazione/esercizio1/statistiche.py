values = []
my_file = open('shampoo_sales.txt', 'r')

def my_fun_sum(values):
    sum = 0
    for i in range(len(values)):
        sum += values[i]
    return sum

def my_fun_ave(values):
    ave = 0;
    for i in range(len(values)):
        ave += values[i]

    ave = ave/(len(values))
    return ave

def my_fun_min(values):
    min = 1000
    for i in range(len(values)):
        if(min > values[i]):
            min = values[i]
    return min

def my_fun_max(values):
    max = 0
    for i in range(len(values)):
        if(max < values[i]):
            max = values[i]
    return max

for line in my_file:
    elements = line.split(',')
    
    if elements [0] != 'Date':
        date  = elements [0]
        value = elements [1]

        values.append(float(value))
        
        my_fun_sum(values)
        my_fun_ave(values)
        my_fun_min(values)
        my_fun_max(values)

print("Somma: {}" .format (my_fun_sum(values)) )
print("Media: {}" .format (my_fun_ave(values)) )
print("Minimo: {}" .format (my_fun_min(values)) )
print("Massimo: {}" .format (my_fun_max(values)) )