# Details of the QED-CAS and QED-FCI Calculations

- The QED-CASCI, QED-CASSCF, and QED-FCI calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems) 

- Atomic Orbital basis: 6-311G

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle$

- Cavity Frequency: 0.12086 atomic units

- Cavity Coupling Vector: [0., 0., 0.05]

- State Averaging performed over first three singlet states for SA-QED-CASSCF

-  The guess orbitals are are either from QED-RHF orbitals, or, in some difficult-to-converge cases, from previously converged SA-QED-CASSCF canonical orbitals at a similar geometry.  [i.e. use the "save orbital" option for one geometry, and the "use orbital geuss" option for the difficult geometry] 

- Orbital Basis for QED-CASCI and QED-FCI comes from QED-RHF orbitals

- QED-CASCI(4e,No,1ph) and SA-QED-CASSCF(4e,No,1ph) ground state energies vs bond length are found in energies_4_N.txt

- QED-FCI(1ph) ground state energies vs bond length are found in fci_2

- Python script to plot the non-parallelity errors is NPE_vs_Active_space.ipynb

