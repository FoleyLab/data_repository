# Details of the QED-DMRG Calculations

- The DMRG calculations were carried out in the [MOLMPS program](https://arxiv.org/abs/2001.04890) using a bond dimension of 1000, resulting in a truncation of less than $10^{-7}$.

- The convergence criteria was set to an energy difference of $10^{-6}$ between sweeps. 

- The calculations were carried in using photon number states as the photonic basis with the maximum photonic Fock state set to be $|10\rangle$.

- The ordering of the electronic sites was optimized without the cavity using the fiedler algorithm, and the cavity was added as the leftmost site.

- The initial guess for the right block was done using the CI-DEAS warm-up procedure.

- Atomic Orbital basis: cc-pVDZ

- Active Space: (12e,23o,10ph)

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle, ... \hat{U}_{\rm CS}|10\rangle$

- The QED-DMRG data with additional details of the cavity (if present) can be found in the following json files:
  - QED-DMRG/mghplus_dmrg_ccpVDZ.json
  - QED-DMRG/mghplus_dmrg_ccpVDZ_lz_0.01_om_0.136.json
  - QED-DMRG/mghplus_dmrg_ccpVDZ_lz_0.05_om_0.136.json

# Details of the QED-CAS Calculations

- The QED-CASCI, QED-CASSCF calculations were carried out using the  [qed-ci program](https://github.com/mapol-chem/qed-ci/tree/casscf) (casscf branch on linux systems, mac_casscf on mac systems)

- Atomic Orbital basis: cc-pVDZ

- Guess Orbitals for SA-QED-CASSCF come from QED-RHF

- Orbital Basis for QED-CASCI comes from QED-RHF

- Photonic basis: coherent-state basis with basis states $\hat{U}_{\rm CS}|0\rangle, \hat{U}_{\rm CS}|1\rangle, ... \hat{U}_{\rm CS}|10\rangle$

- The QED-CASSCF data with additional details of the cavity (if present) can be found in the following json files:
  - QED-CASSCF/mghplus_casscf_ccpVDZ_lz_0_om_0.json
  - QED-CASSCF/mghplus_casscf_ccpVDZ_lz_0.01_om_0.136.json
  - QED-CASSCF/mghplus_casscf_ccpVDZ_lz_0.05_om_0.136.json

- The QED-CASCI data with additional details of the cavity (if present) can be found in the following json files:
  - QED-CASCI/mghplus_casci_ccpVDZ_lz_0_om_0.json
  - QED-CASCI/mghplus_casci_ccpVDZ_lz_0.01_om_0.136.json
  - QED-CASCI/mghplus_casci_ccpVDZ_lz_0.05_om_0.136.json


