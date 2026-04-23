import numpy as np
from sklearn.linear_model import LogisticRegression

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# -----------------------------
# 1. (2 features)
# -----------------------------
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])  # XOR problem 

# -----------------------------
# 2. Quantum feature map
# -----------------------------
def quantum_features(x):
    qc = QuantumCircuit(2)

    qc.h(0)
    qc.h(1)

    qc.ry(x[0] * np.pi, 0)
    qc.ry(x[1] * np.pi, 1)

    qc.cx(0, 1)

    qc.measure_all()

    sim = AerSimulator()
    result = sim.run(qc).result()

    counts = result.get_counts()
    return list(counts.values())[0]

# -----------------------------
# -----------------------------
X_q = np.array([[quantum_features(x)] for x in X])

# -----------------------------
# 4. Classical ML model
# -----------------------------
model = LogisticRegression()
model.fit(X_q, y)

# -----------------------------
# -----------------------------
print("Predictions:")
print(model.predict(X_q))