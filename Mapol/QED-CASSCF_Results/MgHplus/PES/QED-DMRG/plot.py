import matplotlib.pyplot as plt

# Read data
bond_lengths = []
e0 = []
e1 = []
e2 = []

with open("energies.dat") as f:
    next(f)  # Skip header
    for line in f:
        parts = line.split()
        bond_lengths.append(float(parts[0]))
        e0.append(float(parts[1]))
        e1.append(float(parts[2]))
        e2.append(float(parts[3]))

# Plot
plt.figure(figsize=(8, 6))
plt.plot(bond_lengths, e0, label='$\lambda = 0.00$', color='r')
plt.plot(bond_lengths, e1, color='r')
plt.plot(bond_lengths, e2, color='r')

# Read data
bond_lengths = []
e0 = []
e1 = []
e2 = []

with open("energies_0-01.dat") as f:
    next(f)  # Skip header
    for line in f:
        parts = line.split()
        bond_lengths.append(float(parts[0]))
        e0.append(float(parts[1]))
        e1.append(float(parts[2]))
        e2.append(float(parts[3]))

# Plot
plt.plot(bond_lengths, e0, label='$\lambda = 0.01$', color='b')
plt.plot(bond_lengths, e1, color='b')
plt.plot(bond_lengths, e2, color='b')

# Read data
bond_lengths = []
e0 = []
e1 = []
e2 = []

with open("energies_0-05.dat") as f:
    next(f)  # Skip header
    for line in f:
        parts = line.split()
        bond_lengths.append(float(parts[0]))
        e0.append(float(parts[1]))
        e1.append(float(parts[2]))
        e2.append(float(parts[3]))

# Plot
plt.plot(bond_lengths, e0, label='$\lambda = 0.05$', color='g')
plt.plot(bond_lengths, e1, color='g')
plt.plot(bond_lengths, e2, color='g')

plt.xlabel('Bond Length (Å)')
plt.ylabel('Energy (a.u.)')
plt.title('DMRG Energies vs. Bond Length')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("energies_vs_bond_length.pdf")
plt.show()

