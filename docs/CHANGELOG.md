# Changelog

All notable changes to the Year Planner Generator.

## Versioning

- **Format:** `vX.Y` (milestone-based)
- **Scope:** Config, generator, and output share the same version

| Version | Meaning |
|---------|---------|
| v0.x | Development — building sections incrementally |
| v1.0 | First complete release — all sections + final testing |
| v1.x | Refinements and bug fixes |
| v2.0+ | Major redesign or new features |

---

## [Unreleased]

No unreleased changes.

---

## [1.0] — 2026-01-28

### Summary
First complete release — all planned sections implemented and tested.

### Sections Included
- Cover Page (front and inside with contact info)
- Instructions Page (full-page image with overlay)
- Calendar (current year + next year grids)
- Table of Contents (pre-calculated page numbers)
- Goals Page
- Backlog Section
- Week Planner (ISO 8601 week numbering)
- Monthly Sections (×12 month covers + daily spreads)
- Terms and Definitions
- Graph Paper
- Rear Cover (reserved)

### Tested
- All sections generate correctly
- Page flow verified for duplex printing
- Recto/verso layout confirmed
- PDF output working

---

## [0.16] — 2026-01-28

### Added
- Terms and Definitions section with configurable page count and row count
- Two-column table layout (Term/Abbreviation | Definition) with configurable width split
- TOC entries for Terms and Definitions pages with section shading

### Changed
- Section order: Monthly Sections → Terms and Definitions → Graph Paper

---

## [0.15] — 2026-01-27

### Added
- Instructions page with full-page image and transparent title overlay
- File lock error handling documentation

### Changed
- Lowered page number position by 2mm (0.75 → 0.55 cm)
- Table line colors reviewed and adjusted

### Fixed
- Extra blank page after instructions (removed redundant page break)

---

## [0.14] — 2026-01-27

### Added
- Table of Contents with pre-calculated page numbers
- Dynamic TOC column widths based on text content
- Two-level TOC shading (section headers and first items)
- Automatic PDF output alongside Word document
- Non-numbered section breaks for rear cover

### Changed
- Daily spread date format: "Month ddd, YYYY-MM-DD, Week N"
- TOC day labels: "Week N, Month ddd, Day" format
- All table borders now use config values

---

## [0.13] — 2026-01-27

### Added
- Monthly sections: 12 month covers and daily spreads
- Config info overlay separate `bottom`/`right`/`left` positioning
- Contact info table label shading
- Terminal output shows document title/year/version

### Fixed
- Correct recto/verso page tracking for monthly sections
- Minimized page breaks on full pages
- Overlay anchoring for full-page content

---

## [0.12] — 2026-01-26

### Added
- Page numbering with different odd/even footers
- Four separate page margins (top, bottom, left, right)

### Changed
- Recto pages: page number bottom-right
- Verso pages: page number bottom-left
- Dynamic table height recalculation for new margins

---

## [0.11] — 2026-01-26

### Added
- `validate_table_height()` with terminal warnings
- Green debug lines for header/footer boundaries
- Margin-aware graph paper image caching
- Calendar month name shading
- UTF-8 console encoding fix for Windows

### Changed
- Dynamic calendar height (removed fixed config)

---

## [0.10] — 2026-01-26

### Added
- Configurable overlay width parameter
- Comprehensive lessons learned documentation

### Fixed
- Calendar section structure (no extra blank pages)
- Config info overlay positioning

---

## [0.9] — 2026-01-26

### Added
- Configurable table styling (title, header, content rows)
- Configurable border settings via config.yaml
- Universal fixed row height rule (`hRule="exact"`)

---

## [0.8] — 2026-01-26

### Added
- Backlog section with configurable page/row count
- Double-sided backlog tables

### Changed
- Section order: Goals → Backlog → Week Planner

---

## [0.7] — 2026-01-26

### Added
- Goals page with configurable columns and rows

---

## [0.6] — 2026-01-25

### Added
- Config info overlay on all pages
- Configurable overlay font sizes
- Auto-fit text box sizing
- Dynamic height calculation

---

## [0.5] — 2026-01-25

### Added
- Calendar section (current + next year grids)
- Graph paper with PNG images
- Debug visualization (DrawingML red/blue lines)
- Mirror margins with gutter
- Rear cover (blank, reserved)

---

## [0.4] — 2026-01-23

### Changed
- A4 page format (21.0 × 29.7 cm)
- Metric measurement system throughout
- Recalculated column widths for A4

---

## [0.3] — 2026-01-23

### Added
- ISO 8601 week numbering
- First-week-of-month shading (#F2F2F2)
- Optimized last table (no empty rows)
- Prettified terminal output with header box

---

## [0.2] — 2026-01-23

### Added
- Week Planner with dynamic row height calculation
- Minimized page breaks
- Standardized table styling
- Instructions placeholder

---

## [0.1] — 2026-01-23

### Added
- Cover pages (front and inside)
- Rear cover with 2×6 calendar grid
- 0.6cm margins
- Automatic backup

---

## [0.0] — 2026-01-23

### Added
- Initial project setup
- Directory structure
- Documentation framework
- Configuration files
