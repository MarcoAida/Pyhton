#Si consideri una matrice di caratteri 8 × 8 che contiene la posizione di una partita di scacchi. I pezzi bianchi sono rappresentati dalla loro iniziale minuscola: r, d, a, c, t, e p rispettivamente per re, donna, alfiere, cavallo, torre e pedone; i pezzi neri sono rappresentati dalla stessa iniziale maiuscola R, D, A, C, T, e P. Le caselle vuote sono rappresentate dallo spazio. Ad esempio la seguente matrice rappresenta la posizione iniziale. 

#Si vuole scrivere una funzione che valuti chi è in vantaggio nella posizione corrente dal punto di vista del materiale presente sulla scacchiera.

#A questo scopo si usi la seguente valutazione dei pezzi: pedone = 1, cavallo = 3, alfiere = 3, torre = 5, donna = 9, re =0.

#Si scriva un programma python (opportunamente modularizzato tramite funzioni ausiliarie) che prenda come parametro un file contenente una matrice siffatta e restituisca: • 1 se il bianco ha più materiale del nero, • 2 se il nero ha più materiale del bianco, • 0 se il materiale è pari, • -1 se la posizione sulla scacchiera non è legale (ci sono più pezzi di quelli ammessi per tipo [1 re, 1 dama, 2 cavalli,torri,alfieri 8 pedoni ] oppure ci sono pedoni nella prima o ultima riga)

