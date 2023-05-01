# Build circuit
from qiskit.circuit.library import QuantumVolume
circuit = QuantumVolume(5)
# Transpile circuit
from qiskit import transpile
transpiled_circuit = transpile(circuit, basis_gates=['sx', 'rz', 'cx'])
transpiled_circuit.draw()