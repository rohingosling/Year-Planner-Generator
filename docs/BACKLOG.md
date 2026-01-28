# Project Backlog

Task tracking and velocity metrics for the Year Planner Generator.

## Velocity Summary

| Phase | Versions | Tasks | Effort | Focus |
|-------|----------|-------|--------|-------|
| Foundation | v0.0–v0.4 | 10 | 17 | Project setup, cover, week planner, A4 conversion |
| Layout | v0.5–v0.8 | 10 | 22 | Calendar, graph paper, gutter, goals, backlog |
| Styling | v0.9–v0.12 | 11 | 18 | Configurable tables, page numbering, margins |
| Content | v0.13–v1.0 | 19 | 33 | Monthly sections, TOC, instructions, PDF output, terms, release |
| **Total** | | **50** | **90** | |

**Average velocity:** ~22.5 effort per phase

---

## Daily Velocity

| Date | Versions | Tasks | Effort |
|------|----------|-------|--------|
| 2026-01-23 | v0.0–v0.4 | 10 | 17 |
| 2026-01-24 | — | 0 | 0 |
| 2026-01-25 | v0.5–v0.6 | 7 | 18 |
| 2026-01-26 | v0.7–v0.12 | 13 | 22 |
| 2026-01-27 | v0.13–v0.15 | 17 | 28 |
| 2026-01-28 | v0.16–v1.0 | 3 | 5 |
| **Total** | | **50** | **90** |
| **Average** | | **10.0** | **18.0** |
| **Min** | | **3** | **5** |
| **Max** | | **17** | **28** |

*Average, Min, and Max exclude days with zero tasks.*

---

## Completed

| Version | Size | Effort | Task | Description |
|---------|------|--------|------|-------------|
| v0.0 | XS | 1 | Project Setup | Initial project setup and initialization |
| v0.1 | S | 2 | Cover Pages | Front cover (title, version, year) and inside cover (contact info) |
| v0.2 | XS | 1 | Instructions Page | Usage instructions and guidelines (placeholder template) |
| v0.2 | L | 5 | Week Planner | Weekly overview tables with computed row heights for page-fill |
| v0.3 | XS | 1 | ISO 8601 Week Numbers | Week numbering using ISO 8601 standard via `isocalendar()` |
| v0.3 | XS | 1 | First Week Shading | Light gray (#F2F2F2) shading for first week of each month |
| v0.3 | XS | 1 | Last Table Optimization | Last Week Planner table excludes empty rows |
| v0.3 | S | 2 | Terminal Output | Prettified generator output with header box and usage info |
| v0.4 | S | 2 | A4 Page Format | Changed from US Letter to A4 (21.0 × 29.7 cm) |
| v0.4 | XS | 1 | Metric Conversion | Changed all measurements from imperial (inches) to metric (cm) |
| v0.5 | S | 2 | Gutter | Mirror margins with configurable gutter for duplex binding |
| v0.5 | M | 3 | Debug Visualization | Red rectangle (content area) and blue line (gutter) using DrawingML |
| v0.5 | M | 3 | Calendar Section | Current year and next year 2×6 calendar grids on separate pages |
| v0.5 | M | 3 | Graph Paper | Grid paper pages with configurable colors and dimensions |
| v0.5 | XS | 1 | Rear Cover | Blank recto and verso (reserved for future barcode/branding) |
| v0.5 | XS | 1 | Graph Paper Blank Pages | Fixed extra blank pages by anchoring overlays to existing paragraphs |
| v0.6 | L | 5 | Config Info Overlay | Text box overlay showing all config fields, configurable font sizes, auto-fit sizing |
| v0.7 | S | 2 | Goals Page | Long-term goals section |
| v0.8 | S | 2 | Backlog Section | Unscheduled tasks/ideas pages |
| v0.9 | M | 3 | Configurable Table Styling | All table row types (title, header, content) and borders configurable via config.yaml |
| v0.10 | XS | 1 | Config Info Overlay Width | Added configurable width parameter for config info overlay text box |
| v0.10 | S | 2 | Calendar Section Fix | Fixed extra blank pages and overlay positioning in calendar section |
| v0.11 | S | 2 | Table Height Validation | Added `validate_table_height()` function with terminal warnings when tables won't fit |
| v0.11 | XS | 1 | Green Debug Lines | Added green horizontal lines showing header/footer text region boundaries |
| v0.11 | S | 2 | Dynamic Calendar Height | Removed fixed `calendar.height` config; height now calculated dynamically to fill page |
| v0.11 | XS | 1 | Margin-Aware Graph Paper Cache | Graph paper image filenames include pixel dimensions for automatic regeneration on layout changes |
| v0.11 | XS | 1 | Calendar Month Shading | Month names in calendar tables use header row background grayscale for consistent styling |
| v0.11 | XS | 1 | UTF-8 Console Encoding | Fixed Unicode box-drawing characters in terminal output on Windows |
| v0.12 | M | 3 | Page Numbering | Logical page numbers in footers with different odd/even alignment |
| v0.12 | XS | 1 | Separate Page Margins | Four separate margin values (top, bottom, left, right) instead of single margin |
| v0.13 | XL | 8 | Monthly Sections | Month covers and daily spread tables (×12) with correct page tracking |
| v0.13 | XS | 1 | Contact Info Shading | Shading on contact info label cells using header row background grayscale |
| v0.13 | XS | 1 | Document Info in Terminal | Terminal output shows document title, year, and version after loading config |
| v0.13 | XS | 1 | Year Test | Tested generating documents for 2024, 2026, 2027 - all stable |
| v0.13 | XS | 1 | Flexible Overlay Position | Config info overlay uses separate `bottom`, `right`, `left` positioning instead of single `margin` |
| v0.13 | XS | 1 | Cell Shading Utility | Added `set_cell_shading()` function to tables.py for grayscale cell backgrounds |
| v0.14 | L | 5 | Table of Contents | Custom table-based TOC/Index with pre-calculated page numbers, entries for all numbered pages, configurable rows per page, dynamic column widths |
| v0.14 | XS | 1 | TOC Column Optimization | Dynamic TOC column widths based on text content with separate label and page number padding |
| v0.14 | XS | 1 | TOC Day Label Format | TOC day entries use "Week N, Month ddd, Day" format for easy week identification |
| v0.14 | XS | 1 | Daily Spread Date Format | Updated date string to "Month ddd, YYYY-MM-DD, Week N" with ISO date and week number |
| v0.14 | XS | 1 | PDF Output | Generator automatically creates PDF alongside Word document using docx2pdf |
| v0.14 | XS | 1 | Non-Numbered Section Break | Added `add_non_numbered_section_break()` for sections without page numbers (rear cover) |
| v0.15 | S | 2 | Instructions Page Image | Full-page instructions image with transparent title overlay using DrawingML floating text box |
| v0.15 | XS | 1 | Page Number Position | Lowered page number position by 2mm (0.75 → 0.55 cm) for better visual balance |
| v0.15 | XS | 1 | File Lock Error Handling | Added documentation for handling file lock errors - stop, ask user to close, retry |
| v0.15 | XS | 1 | Table Line Color | Review and test different table and line element colors for a more elegant appearance |
| v0.16 | S | 2 | Terms and Definitions Section | New section with two-column tables for recording terms and definitions |
| v0.16 | XS | 1 | Terms and Definitions TOC | Added TOC entries for Terms and Definitions pages with section shading |
| v1.0 | S | 2 | Final Testing | Comprehensive testing of all sections, page flow, duplex printing, and visual inspection |

---

## In Progress

*No tasks currently in progress.*

---

## Planned

| Size | Effort | Task | Description |
|------|--------|------|-------------|
| L | 5 | Advanced Formatting | Generate custom page layouts as images with advanced formatting elements not available directly in MS Word |
| S | 2 | Sales and Marketing | Research formal design for Amazon distribution |
| - | - | Add project to GitHub | Add the project to my Github |

---

## Size/Effort Key

| Size | Effort Points | Description |
|------|---------------|-------------|
| XS | 1 | Extra Small — trivial fix, config tweak, < 30 min |
| S | 2 | Small — minor feature, single-file change, < 1 hour |
| M | 3 | Medium — modest feature, multi-file change, 1–3 hours |
| L | 5 | Large — significant feature, new module, 3–6 hours |
| XL | 8 | Extra Large — major feature, architectural change, 6–12 hours |
| XXL | 13 | Epic — multi-day effort (decomposition trigger) |

Fibonacci scale for relative sizing.
