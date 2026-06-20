# Heterojunction Construction Workflow

## Practical Lessons

- GUI or commercial modeling-tool automation can be fragile across installations. Prefer deterministic Python structure building unless the target automation interface is verified live.
- Some VESTA-exported CIF files may use occupancy `0.0000` for all atoms; generated structures should use full occupancy unless disorder is being modeled.
- `C3N4.cif` used symmetry operations and a non-P1 space group. Expand symmetry before supercell construction; otherwise the model will miss atoms.
- Always keep a JSON metadata file recording input paths, supercell matrices, mismatch, layer thickness, interface gap, vacuum, atom counts, and fixed atoms.

## Proven Examples

### BiOI(001)/CdS(110)

- Inputs: `BiIO.cif`, `CdS.cif`.
- BiOI slab: `(001)`, two z repeats.
- CdS slab: `(110)` with in-plane basis `[1 -1 0]` and `[0 0 1]`, normal `[1 1 0]`.
- Literature-derived initial interface gap: `3.87 A` from CdS/BiOI oxygen-vacancy heterojunction literature. Treat it as a starting distance for relaxation.
- Example output had `136` atoms, `15 A` top vacuum, and fixed bottom BiOI atoms.

### g-C3N4(001)/BiOI(001)

- Direct literature: RSC/PCCP `10.1039/D2CP04583D`, triazine-based `g-C3N4/BiOI(001)`.
- Literature model: monolayer `1 x 5` g-C3N4 matched to three-layer `2 x 6` BiOI(001), mismatch reported as `3.92% / 0.07%`.
- Figure 3 labels interface distance before relaxation as `3.68 A` and after relaxation as `2.92 A`. Use `3.68 A` for an initial optimization model.
- A low-mismatch model for one set of CIFs used C3N4 matrix `[[4,4],[-1,1]]` and BiOI matrix `[[7,0],[0,3]]`, producing `364` atoms and mismatch `0.49% / 1.52%`.
- A speed model used C3N4 matrix `[[-3,-2],[-1,-2]]` and BiOI matrix `[[-4,-2],[-1,-3]]`, producing `176` atoms with length mismatch `3.96% / 3.75%` and angle difference about `4.11 deg`. This is acceptable when speed is explicitly prioritized speed and k-point sampling; it is not the best low-mismatch model.

## Matching Heuristics

- Generate candidate 2D integer matrices for each material.
- Compare vector lengths and in-plane angles. For oblique cells, report both length mismatch and angle mismatch.
- Prefer smaller area only after satisfying the requested mismatch tolerance.
- For property calculations, avoid very high mismatch even if a smaller model runs faster; interface strain can dominate charge transfer and band alignment.
- If the chosen small model exceeds 3% but stays under 5%, explicitly state the tradeoff and keep the lower-mismatch model as a reference.

## Slab and Property Guidance

- PDOS can be computed for bulk-like or slab structures, but interface PDOS should use the relaxed heterojunction slab.
- Work function requires a slab with vacuum. For asymmetric slabs, add a z-direction dipole correction.
- Charge-density difference needs all component calculations in the exact same cell and geometry partition as the heterojunction.
- Fix only the bottom layers far from the interface for geometry optimization. Do not fix interface atoms unless the request requires a constrained scan.
