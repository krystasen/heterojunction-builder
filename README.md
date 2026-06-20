# Heterojunction Builder Skill

Codex skill for building slab heterojunction models from local CIF/POSCAR files for DFT workflows.

The skill captures a reusable workflow for:

- literature-informed interface distances;
- 2D lattice matching with explicit mismatch reporting;
- slab stacking with vacuum layers;
- POSCAR/CIF/JSON output generation;
- selective dynamics constraints for geometry optimization;
- validation for PDOS, work-function, and charge-density-difference preparation.

## Use Cases

Use this skill when asking Codex to build or validate models such as:

- `BiOI(001)/CdS(110)`;
- `g-C3N4(001)/BiOI(001)`;
- semiconductor slab heterojunctions;
- reduced-size speed models with k-point sampling;
- interface structures for PDOS, work function, electrostatic potential, or charge-density-difference calculations.

## Installation

Copy the `heterojunction-builder` folder into your Codex skills directory:

```text
$CODEX_HOME/skills/heterojunction-builder
```

Then start a new Codex session or reload available skills. The skill should trigger on requests involving heterojunction construction, lattice matching, slab interfaces, vacuum layers, POSCAR/CIF output, or related DFT preparation.

## Typical Workflow

1. Provide the local CIF/POSCAR input files and requested facets.
2. Search the literature for the same or closest heterojunction.
3. Use the reported interface distance as an initial geometry parameter.
4. Search integer 2D supercell matches and report length and angle mismatch.
5. Build the slab interface with sufficient vacuum, typically `15 A`.
6. Add selective dynamics constraints for geometry optimization when appropriate.
7. Write `CIF`, `POSCAR`, and `JSON` metadata.
8. Re-read the generated structure and validate geometry before running DFT.

## Outputs

A complete build should usually include:

- a generated structure file such as `*.cif`;
- a VASP-style `POSCAR` with optional `Selective dynamics`;
- a metadata file such as `*.json`;
- a project-local builder script so the model can be regenerated;
- a short summary of lattice mismatch, strain, interface distance, vacuum thickness, fixed atoms, and suggested k-point grids.

## Notes

- Prefer mismatch below `3%` when possible.
- Accept mismatch below `5%` only when speed is prioritized and the tradeoff is reported.
- Treat literature interface distances as initial model parameters unless the source explicitly reports the final relaxed distance.
- For asymmetric slab work-function calculations, use a vacuum region and z-direction dipole correction.
- For charge-density difference, use the same cell, grid, and atomic positions for the heterojunction and isolated component slabs.
