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
        lenght = len(data)
        l = []
        im = 0
        if(data != None and lenght > 1): # Logica per la predizione
            for i in l:
                l[i+1] = l[3] + t[i-1]
                im = t
                
        prediction = im/n
        return prediction
