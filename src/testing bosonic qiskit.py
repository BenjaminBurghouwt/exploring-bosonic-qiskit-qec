import c2qa
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumRegister, ClassicalRegister


def main():
    n_modes = 1
    n_qubits = 1
    cutoff = 2 ** 4
    alpha = 3 / np.sqrt(2)

    qmr = c2qa.QumodeRegister(num_qumodes=n_modes, num_qubits_per_qumode=int(np.ceil(np.log2(cutoff))))

    qbr = QuantumRegister(n_qubits)
    cbr = ClassicalRegister(n_qubits)

    circuit = c2qa.CVCircuit(qmr, qbr, cbr)

    circuit.draw('mpl')


if __name__ == "__main__":
    main()
