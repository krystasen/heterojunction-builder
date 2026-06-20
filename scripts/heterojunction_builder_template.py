"""Template for deterministic slab heterojunction builders.

Copy this file into the project folder and customize:
- input paths
- surface/facet transforms
- supercell matrices
- interface gap and vacuum
- element order and output names

The template intentionally leaves the material-specific builder functions
unimplemented so the agent reviews the geometry choices for each system.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VACUUM_ANGSTROM = 15.0


def main() -> None:
    raise NotImplementedError(
        "Copy this template into the project directory and implement the "
        "material-specific CIF parsing, lattice matching, slab stacking, "
        "CIF/POSCAR writing, and validation metadata."
    )


def write_metadata(path: Path, metadata: dict) -> None:
    path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
