"""Esempio introduttivo: analisi di dati e regressione con PyTorch."""

# PyTorch e TensorFlow sono entrambi framework di machine learning.
# Qui usiamo solo PyTorch; TensorFlow/Keras è un'alternativa.

import torch
from torch import nn

torch.manual_seed(0)

# Dataset sintetico: i valori seguono all'incirca la relazione y = 3x + 2.
x = torch.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * x + 2 + torch.randn_like(x) * 1.5

# Una rapida occhiata ai dati.
print(f"Numero di osservazioni: {len(x)}")
print(f"Media di x: {x.mean():.2f}; media di y: {y.mean():.2f}")
correlation = torch.corrcoef(torch.stack((x[:, 0], y[:, 0])))[0, 1]
print(f"Correlazione x-y: {correlation:.2f}")

# Usa le prime 80 osservazioni per l'addestramento e le restanti per il test.
x_train, y_train = x[:80], y[:80]
x_test, y_test = x[80:], y[80:]

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for _ in range(500):
	loss = loss_fn(model(x_train), y_train)
	optimizer.zero_grad()
	loss.backward()  # Calcola i gradienti.
	optimizer.step()  # Aggiorna peso e bias.

with torch.no_grad():
	test_loss = loss_fn(model(x_test), y_test)

print(f"\nRetta stimata: y = {model.weight.item():.2f}x + {model.bias.item():.2f}")
print(f"Errore MSE sul test: {test_loss.item():.2f}")

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.scatter(x, y, label="Dati", alpha=0.5)
    plt.plot(x, model(x).detach(), color="red", label="Retta stimata")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Regressione lineare con PyTorch")
    plt.legend()
    plt.show()
