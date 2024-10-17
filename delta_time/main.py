from datetime import datetime, timedelta

# Prendiamo l'orario corrente
ora_corrente = datetime.now()

# Sottraiamo 15 ore e 30 minuti
tempodasottrarre = timedelta(hours=15, minutes=30)
tempo_sottratto = ora_corrente - tempodasottrarre

# Sommiamo 15 ore e 30 minuti
tempodasommare = timedelta(hours=6, minutes=30)
tempo_sommato = ora_corrente + tempodasommare

# Mostriamo l'ora risultante
print(tempo_sottratto)
print(tempo_sommato)
