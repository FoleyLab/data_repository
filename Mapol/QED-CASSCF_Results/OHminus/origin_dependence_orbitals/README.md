# Details of the QED-CASSCF Calculations

- QED-CASSCF calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems)

- Atomic Orbital basis: 6-31G

- Guess Orbitals for CS-QED-CASSCF come from QED-RHF

- Guess Orbitals for PN-QED-CASSCF come from RHF

- State averaging is [Add if relevant]

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle$

- The CS-QED-CASSCF(6e,6o,1ph) Canonical Orbitals transformation vectors at the origin and at displacement are found in 'oh_m_cs/orbital_6_6_1.out' and 'oh_m_cs/orbital_6_6_2.out', respectively

- The CS-QED-CASSCF(6e,6o,1ph) Natural Orbitals transformation vectors at the origin and at displacement are found in 'oh_m_cs/natural_orbital_6_6_1.out' and 'oh_m_cs/orbital_6_6_2.out', respectively with occupation numbers found in  'oh_m_cs/occupation_number_6_6_1.out' and 'oh_m_cs/occupation_number_6_6_2.out', respectively

- The PN-QED-CASSCF(6e,6o,1ph) Canonical Orbitals transformation vectors at the origin and at displacement are found in 'oh_m_pn/orbital_6_6_1.out' and 'oh_m_pn/orbital_6_6_2.out', respectively

- The PN-QED-CASSCF(6e,6o,1ph) Natural Orbitals transformation vectors at the origin and at displacement are found in 'oh_m_pn/natural_orbital_6_6_1.out' and 'oh_m_pn/orbital_6_6_2.out', respectively with occupation numbers found in  'oh_m_pn/occupation_number_6_6_1.out' and 'oh_m_pn/occupation_number_6_6_2.out', respectively

- Plot scripts 'oh_m_pn/OH_Plot.ipynb' and 'oh_m_cs/OH_Plot.ipynb'  read the orbital transformation vectors, write them to cube files, and plot them
