from qiskit import QuantumCircuit, transpile
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Standard Decomposition Circuit
# ---------------------------------------------------------
qc = QuantumCircuit(3)
qc.ccx(0, 1, 2)  # CCNOT on qubits 0, 1 (controls) and 2 (target)
decomposed = qc.decompose()

# Generate a matplotlib figure of the circuit using a publication-friendly style
# style='bw' uses black and white, perfect for print journals like PRD
fig_std = decomposed.draw(output='mpl', style='bw', scale=1.2)

# Save as high-resolution PNG and vector PDF
fig_std.savefig('toffoli_standard_decomposition.pdf', format='pdf', bbox_inches='tight')
fig_std.savefig('toffoli_standard_decomposition.png', dpi=600, bbox_inches='tight')
plt.close(fig_std)

# ---------------------------------------------------------
# 2. Custom Transpiled Circuit (RX, RY, RZ, CX)
# ---------------------------------------------------------
custom_circuit = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'cx'], optimization_level=3)

# Generate figure for the custom transpiled circuit
fig_cust = custom_circuit.draw(output='mpl', style='bw', scale=1.2)

# Save high-res output
fig_cust.savefig('toffoli_custom_transpiled.pdf', format='pdf', bbox_inches='tight')
fig_cust.savefig('toffoli_custom_transpiled.png', dpi=600, bbox_inches='tight')
plt.close(fig_cust)

print("Circuits successfully exported as PRD-ready PDF and PNG files!")