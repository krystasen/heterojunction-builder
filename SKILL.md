---
name: heterojunction-builder
description: Build computational slab heterojunction models from local CIF/POSCAR inputs for DFT workflows. Use when the request asks to construct, shrink, validate, or prepare interface structures such as BiOI/CdS, g-C3N4/BiOI, semiconductor heterojunctions, surface-slab interfaces, POSCAR/CIF outputs, lattice matching, interface distance from literature, vacuum layers, selective dynamics, PDOS, work function, or charge-density-difference preparation.
---

# Heterojunction Builder

## Workflow

1. Read the exact local inputs provided in the request. Do not assume primitive cells are P1; parse CIF symmetry when present.
2. Identify surfaces and slab orientation. For simple `(001)` slabs, stack along `z`; for nontrivial facets, explicitly define the in-plane and normal basis.
3. Search current literature for the same or closest heterojunction. Extract interface distance, layer count, mismatch, and whether the reported value is pre- or post-relaxation. Cite sources in the final answer.
4. Search 2D lattice matches before building. Prefer mismatch under 3%; accept under 5% only when speed is prioritized speed and k-point sampling. Report angle mismatch separately from length mismatch.
5. Build the slab heterojunction with enough vacuum, normally `15 A` along `z`. Preserve enough substrate thickness for surface/interface properties.
6. Write `CIF`, `POSCAR`, and `JSON` metadata. Use `Selective dynamics` in POSCAR when relaxation constraints are needed.
7. Independently re-read the output and validate atom counts, cell, vacuum, interface gap, nearest cross-interface contact, mismatch, and fixed-atom region.

For detailed local conventions and lessons from BiOI/CdS and g-C3N4/BiOI, read [references/workflow.md](references/workflow.md). For validation commands and thresholds, read [references/validation.md](references/validation.md).

## Implementation Guidance

- Prefer script-based construction over GUI automation when Materials Studio scripting is unavailable or unstable.
- Use structured parsers when available (`pymatgen`, `ase`). If unavailable, implement a CIF reader that handles loop headers, symmetry operations, occupancies, and fractional coordinates.
- Keep original input files unchanged. Create a named builder script beside outputs so the model can be regenerated.
- For VESTA-exported CIF files with `0.0000` occupancies, write generated atoms with occupancy `1.0000` unless partial occupancy treatment is explicitly required.
- Store literature-derived values in metadata as "initial model" values when they are pre-relaxation distances. Do not present the initial interface gap as the final relaxed distance.
- For speed models, keep the validated larger/low-mismatch model and create a separate `small`, `speed`, or atom-count-labeled output.

## Model Defaults

- Vacuum: `15 A` minimum along `z` for slab/interface calculations.
- Interface gap: literature value if available; otherwise use a chemically reasonable starting distance and label it as provisional.
- Relaxation constraints: fix the bottom substrate region far from the interface; relax the interface, adsorbed/top material, and upper substrate layers.
- Static properties: compute PDOS, work function, and charge-density difference from the relaxed geometry in the same cell.
- Charge-density difference: require heterojunction, isolated slab A, and isolated slab B with identical cell, grid, atomic positions, and calculation settings.
- Work function: use a slab model with vacuum and z-direction dipole correction for asymmetric slabs.

## Reusable Scripts

Use [scripts/heterojunction_builder_template.py](scripts/heterojunction_builder_template.py) as a starting point when creating a new deterministic builder. Copy it into the project directory, fill in the materials, matrices, interface gap, vacuum, and output names, then run and validate it. Do not use it as a black box without reviewing the chosen lattice match.
