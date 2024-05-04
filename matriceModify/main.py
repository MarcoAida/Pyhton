#Sia dato un file che contiene una matrice rettangolare di interi positivi preceduta dalle sue dimensioni (separate dal carattere “X”)

#Come esempio si consideri il file “in.txt” con il seguente contenuto (5X6)

#Scrivere uno script python che prenda il nome di un file e produca un file “out.txt” eliminando le righe che hanno come primo valore 0 ed invertendo l’ordine delle righe.

#Il numero di righe (nella prima riga, quella delle dimensioni) deve essere riscritto in modo che corrisponda alle righe della nuova matrice.

#Nell’esempio di cui sopra il contenuto del file al termine dell’esecuzione deve essere il seguente (3X6):

#2 3 3 3 0 1
#3 2 5 2 0 0
#1 3 4 8 9 5

myfile = open("in.txt", "r")

l = myfile.readline()

l = l.split("X")

print(l)

#for i in myfile:
#l = myfile.readline()
#print(l)

#for line in myfile:
#for i in l:
#if line[0] == "0":
#l.remove(line)

#for line in myfile:
#myfile.reverse()
#myfile = open("out.txt", "w")

myfile.flush()

myfile.close()

#if __name__ == "__main__":
