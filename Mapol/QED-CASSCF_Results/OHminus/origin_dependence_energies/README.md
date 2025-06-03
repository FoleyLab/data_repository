# Details of the QED-CASSCF Calculations

- The QED-CASCI, QED-CASSCF calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems)

- Atomic Orbital basis: cc-pVDZ

- Guess Orbitals for SA-QED-CASSCF come from [Nam Include Details Here]

- State averaging is performed over the three lowest singlet states (ground state, lower polariton, upper polariton) with equal weighting

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle, ... \hat{U}_{\rm CS}|10\rangle$

- The QED-CASSCF data with additional cavity details can be found in 
    - pn_casscf_2e2o.txt_analysis.json				
    - cs_casscf_2e2o.txt_analysis.json	
    - pn_casscf_6e6o.txt_analysis.json
    - cs_casscf_6e6o.txt_analysis.json	

