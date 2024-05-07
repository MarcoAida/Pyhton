#Si consideri una matrice di caratteri 8 × 8 che contiene la posizione di una partita di scacchi. I pezzi bianchi sono rappresentati dalla loro iniziale minuscola: r, d, a, c, t, e p rispettivamente per re, donna, alfiere, cavallo, torre e pedone; i pezzi neri sono rappresentati dalla stessa iniziale maiuscola R, D, A, C, T, e P. Le caselle vuote sono rappresentate dallo spazio. Ad esempio la seguente matrice rappresenta la posizione iniziale.

#Si vuole scrivere una funzione che valuti chi è in vantaggio nella posizione corrente dal punto di vista del materiale presente sulla scacchiera.

#A questo scopo si usi la seguente valutazione dei pezzi: pedone = 1, cavallo = 3, alfiere = 3, torre = 5, donna = 9, re =0.

#Si scriva un programma python (opportunamente modularizzato tramite funzioni ausiliarie) che prenda come parametro un file contenente una matrice siffatta e restituisca: • 1 se il bianco ha più materiale del nero, • 2 se il nero ha più materiale del bianco, • 0 se il materiale è pari, • -1 se la posizione sulla scacchiera non è legale (ci sono più pezzi di quelli ammessi per tipo [1 re, 1 dama, 2 cavalli,torri,alfieri 8 pedoni ] oppure ci sono pedoni nella prima o ultima riga)

# dizionario pedone = 1, cavallo = 3, alfiere = 3, torre = 5, donna = 9, re = 0

myPoint = {"p": 1, "c": 3, "a": 3, "t": 5, "d": 9, "r": 0}

myValue = {"p": 8, "c": 2, "a": 2, "t": 2, "d": 1, "r": 1}

#myValueB = {"P": 8, "C": 2, "A": 2, "T": 2, "D": 1, "R": 1}

maxlen = sum(myValue.values())
#print("maxlen: {}".format(maxlen))


def read_file(filename):
    
    try:
        with open(filename, "r") as myfile:
            for line in myfile:
                print(line.strip())
                
    except FileNotFoundError:
        print("The file was not found.")
        
    except IOError:
        print("Error opening the file.")


def check_advantage(lenWhite, lenBlack):

    maxpoint = 0

    for i in myPoint.keys():
        maxpoint += myValue.get(i, 0) * myPoint.get(i, 0)

    #print("maxpoint: {}".format(maxpoint))

    if lenWhite > maxpoint or lenBlack > maxpoint:
        return -1  #len error
    elif lenWhite > lenBlack:
        return 1  #white
    elif lenWhite < lenBlack:
        return 2  #black
    elif lenWhite == lenBlack:
        return 0  #pari


def check_items(myfile):
    listWhite = []
    listBlack = []

    for line in myfile:
        element = line.strip()
        #print(len(element))
        for i in range(len(element)):
            if element[i] == "r" or element[i] == "d" or element[
                    i] == "a" or element[i] == "c" or element[
                        i] == "t" or element[i] == "p":
                listWhite.append(element[i])
            elif element[i] != " ":
                listBlack.append(element[i])

    return listWhite, listBlack


def check_legal(listWhite, listBlack):
    howmanyWhite = 0
    howmanyBlack = 0

    for piece in listWhite:
        piece = piece.lower()
        # Using get() method on dictionary to retrieve value for piece
        howmanyWhite += myPoint.get(piece, 0)

    for piece in listBlack:
        piece = piece.lower()
        howmanyBlack += myPoint.get(piece, 0)

    return howmanyWhite, howmanyBlack


if __name__ == "__main__":

    print("Executing main block")

    myfile = open("scacchiera.txt", "r")
    #myfile = open("scacchieraBianca.txt", "r")
    #myfile = open("scacchieraNera.txt", "r")
    #myfile = open("scacchieraSbagliata.txt", "r")

    w, b = check_items(myfile)

    print('\n')
    print("White: {}".format(w))
    print("Black: {}".format(b))

    print('\n')
    print("White len: {}".format(len(w)))
    print("Black len: {}".format(len(b)))

    print('\n')
    clw, clb = check_legal(w, b)
    
    adv = check_advantage(clw, clb)
    #1: white, 2: black, 0: pari, -1: howmany error
    print("Result: {}".format(adv))

    print("White point: {}".format(clw))
    print("Black point: {}".format(clb))

    print('\n')
    #myfile = read_file("scacchiera.txt")
    #myfile = read_file("scacchieraBianca.txt")
    #myfile = read_file("scacchieraNera.txt")
    #myfile = read_file("scacchieraSbagliata.txt")
