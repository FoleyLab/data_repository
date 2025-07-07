# =============================
# plot_only_vibronic_analysis.py
# =============================
"""
Load PES data from different QED methods, compute vibrational quantities,
and generate only the final plots you need (removing the unused ones).
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from Necessary_functions import (
    load_pes_data,
    finite_difference_states,
    compute_huang_rhys,
    compute_franck_condon,
    compute_optimal_geometry
)

# --- Configuration ---
DATA_FILE = "pes_data.json"
COUPLING_STRENGTHS = [0.00, 0.01, 0.05, 0.10]
TARGET_STATES = ["ground", "excited", "lower_polariton", "upper_polariton"]
OUTPUT_DIR = "plots/"

# --- Plotting styles ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 14,
    "legend.fontsize": 12,
    "figure.dpi": 300
})

COLORS = {
    "ground": "black",
    "excited": "forestgreen",
    "lower_polariton": "dodgerblue",
    "upper_polariton": "orangered"
}


def main():
    # Load all PES data (dict keyed by method, coupling strength, etc.)
    data = load_pes_data(DATA_FILE)

    for coupling in COUPLING_STRENGTHS:
        # Compute vibrational states on each surface
        vs_ground = finite_difference_states(data, coupling, state="ground")
        vs_excited = finite_difference_states(data, coupling, state="excited")
        vs_lp = finite_difference_states(data, coupling, state="lower_polariton")
        vs_up = finite_difference_states(data, coupling, state="upper_polariton")

        # Plot energies vs bond length for each state
        fig, ax = plt.subplots(figsize=(6, 4))
        for state, vs in zip(TARGET_STATES, [vs_ground, vs_excited, vs_lp, vs_up]):
            bond, energy = vs[:, 0], vs[:, 1]
            ax.plot(bond, energy,
                    label=state.replace("_", " ").title(),
                    color=COLORS[state])

        ax.set_title(f"Energies at coupling λ = {coupling:.2f}")
        ax.set_xlabel("Bond length (Å)")
        ax.set_ylabel("Energy (Hartree)")
        ax.grid(True)
        ax.legend()
        fig.tight_layout()
        fig.savefig(f"{OUTPUT_DIR}energies_lambda_{coupling:.2f}.pdf")
        plt.close(fig)

    print("All plots generated successfully.")


if __name__ == "__main__":
    main()
