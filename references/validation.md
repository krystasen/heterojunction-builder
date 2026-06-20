# Validation Checklist

## Required Checks

- Confirm all requested output files exist: builder script, CIF, POSCAR, JSON metadata.
- Re-read generated POSCAR/CIF rather than trusting the builder's own summary.
- Verify:
  - atom count and element counts;
  - cell lengths and angles;
  - slab z extents and layer thickness;
  - top vacuum equals requested value, normally `15 A`;
  - interface z gap equals the intended initial distance;
  - nearest cross-interface distance is not an overlap;
  - fixed atoms are only in the intended bottom region;
  - no accidental coordinates sit exactly outside the periodic cell.

## Geometry Thresholds

- Length mismatch target: `<3%` preferred; `<5%` acceptable only when speed is prioritized.
- Angle mismatch: report separately; if greater than about `3 deg`, call it out as a speed/strain tradeoff.
- Interface distance: use literature value as initial distance. If nearest 3D contact is much smaller than z gap, inspect lateral registry.
- Vacuum: `15 A` minimum for work-function and electrostatic-potential analysis unless the request requires more.

## Recommended Output Summary

Include:

- output file paths;
- literature source and whether the interface distance is before or after relaxation;
- supercell matrices or repeat counts;
- atom counts by element;
- mismatch and applied strain;
- cell dimensions and vacuum;
- fixed atom count and fixed region;
- suggested k-point grid for optimization and static calculations.

## Windows Command Notes

- Paths often contain spaces; use `-LiteralPath` in PowerShell.
- Avoid dense nested PowerShell quoting for Python snippets. Prefer here-strings piped into `python -`.
