# Details of the QED-CAS and QED-FCI Calculations

- The QED-CASCI, QED-CASSCF, and QED-FCI calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems)

- Atomic Orbital basis: 6-311G

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle, ... \hat{U}_{\rm CS}|10\rangle$

- Cavity Frequency: 0.12086 atomic units

- Cavity Coupling Vector: [0., 0., 0.05]

- State Averaging performed over first three singlet states for SA-QED-CASSCF

- Guess Orbitals for SA-QED-CASSCF come from QED-RHF

- Orbital Basis for QED-CASCI and QED-FCI comes from QED-RHF

- QED-CASCI(4e,9o,10ph) ground state, lower-polariton, and upper-polariton energies are found in LiH_qedcasci_4e_9o_10ph_lz_0.05_om_0.12086.json

- SA-QED-CASCI(4e,9o,10ph) ground state, lower-polariton, and upper-polariton energies are found in LiH_qedcas_4e_9o_10ph_lz_0.05_om_0.12086.json

- QED-FCI(10ph) ground state, lower-polariton, and upper-polariton energies are found in LiH_qedfci_10ph_lz_0.05_om_0.12086.json

- Python script to plot the PES and compute the MAE is LiH_plot.ipynb
