#  Hybrid Quantum Machine Learning Demo

This project demonstrates a simple **Hybrid Quantum-Classical Machine Learning model** using Qiskit and Scikit-learn.

##  Concept
We combine:
- Quantum feature encoding using Qiskit circuits
- Classical ML model (Logistic Regression)

This is a basic example of:
Quantum Machine Learning (QML)

##  Tech Stack
- Qiskit
- Qiskit Aer
- NumPy
- Scikit-learn

##  How to run

```bash
pip install -r requirements.txt
python hybrid.py

```
##  Quantum Feature Encoding
```
We use **Angle Encoding** to transform classical data into quantum states.

Each input feature is mapped to rotation angles applied on qubits using Ry gates.

Additionally, we introduce entanglement using CX gates to capture correlations between features.

This allows the quantum circuit to represent classical data in a higher-dimensional Hilbert space, which can enhance feature separability in some cases.
```
---

## Output
The model predicts simple XOR-like patterns using quantum-enhanced features.

## Note
This is an educational/demo project, not a production quantum advantage model.

---

# 🚫 4. .gitignore

```gitignore id="git1"
__pycache__/
*.pyc
quantum_env/
.env
