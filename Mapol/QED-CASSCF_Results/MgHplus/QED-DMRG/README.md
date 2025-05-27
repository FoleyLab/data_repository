# Details of the QED-DMRG Calculations

- The DMRG calculations were carried out in the [MOLMPS program](https://arxiv.org/abs/2001.04890) using a bond dimension of 1000, resulting in a truncation of less than $10^{-7}$.

- The convergence criteria was set to an energy difference of $10^{-6}$ between sweeps. 

- The calculations were carried in using photon number states as the photonic basis with the maximum photonic Fock state set to be $|10\rangle$.

- The ordering of the electronic sites was optimized without the cavity using the fiedler algorithm, and the cavity was added as the leftmost site.

- The initial guess for the right block was done using the CI-DEAS warm-up procedure.

