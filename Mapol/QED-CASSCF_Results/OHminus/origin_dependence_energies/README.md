# Details of the QED-CASSCF Calculations

- The QED-CASCI, QED-CASSCF calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems)

- Atomic Orbital basis: 6-31G  

- Guess Orbitals for SA-QED-CASSCF(2e, 2o) come from random orbitals 
- Guess Orbitals for SA-CS-CASSCF(6e, 6o) come from QED-HF orbitals 
- Guess Orbitals for SA-PN-CASSCF(6e, 6o) come from RHF orbitals 

- State averaging is performed over only ground state

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle, ... \hat{U}_{\rm CS}|10\rangle$

- The QED-CASSCF data with additional cavity details can be found in 
    - pn_casscf_2e2o.txt_analysis.json				
    - cs_casscf_2e2o.txt_analysis.json	
    - pn_casscf_6e6o.txt_analysis.json
    - cs_casscf_6e6o.txt_analysis.json	

