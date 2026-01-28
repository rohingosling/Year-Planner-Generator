# CLAUDE.md

Project guidance for Claude Code.

## Current Version

**v1.0** — First complete release

## Project Summary

Python document generator producing a configurable Year Planner as a Microsoft Word document, optimized for duplex printing.

## Documentation

- **@README.md** — Human readable overview of the project for Github
- **@docs/SPEC.md** — Product specification (document structure, table layouts, configuration)
- **@docs/ARCHITECTURE.md** — System design, module structure, implementation details
- **@docs/CHANGELOG.md** — Version history
- **@docs/BACKLOG.md** — Task tracking and velocity metrics

## Quick Reference

| Component | Technology |
|-----------|------------|
| Language | Python 3.14+ |
| Document | `python-docx` |
| PDF | `docx2pdf` |
| Config | YAML (`pyyaml`) |

## Commands

```bash
# Activate venv and run generator
.venv/Scripts/python.exe -X utf8 src/main.py

# Windows batch
cmd /c run.bat

# Check for missing dependencies
.venv/Scripts/python.exe scripts/check_deps.py
```

## Code Style

- Type hints on all function signatures
- No magic numbers — use config values
- Each section in its own module under `src/sections/`
- Grayscale values: 0 = white, 100 = black

## Config File Style

Use **section-scoped alignment** — values aligned within their parent mapping, not globally.

```yaml
# Correct
document:
  title:   "Year Planner"
  version: "1.0"
  year:    2026

page:
  width:  21.0
  height: 29.7
```

---

## Do's

| Rule | Rationale |
|------|-----------|
| Update `requirements.txt` when adding new imports | Keeps dependencies in sync; run `scripts/check_deps.py` to verify |
| Maintain strict recto/verso layout | Duplex printing requires odd pages on right, even on left |
| Use Word sections for footer changes | Different headers/footers require document section breaks |
| Use `footer` margin property for page number position | Do NOT use `spacing.before` on footer paragraphs |
| Add explicit page breaks before non-full-page content | Prevents layout drift |
| Verify page flow after adding sections | Check for unintended blank pages |
| Use `hRule="exact"` for all row heights | Prevents font-based row expansion |
| Anchor overlays to existing paragraphs | Adding new paragraphs creates extra blank pages |
| Use minimized page breaks (1pt) for full-page tables | Maximizes available space for table height calculation |

## Don'ts

| Rule | Why It Failed | Fix |
|------|---------------|-----|
| Don't add new imports without updating `requirements.txt` | Missing dependencies break fresh installs | Add to `requirements.txt` immediately |
| Don't add page breaks after full-page content | Tables filling the page cause automatic page advance | Remove explicit breaks after full tables |
| Don't use `spacing.before` on footers | Pushes content area up, breaks table height calculations | Use `footer` margin property instead |
| Don't hardcode measurements in code | Breaks configurability | Always read from `config.yaml` |
| Don't add paragraphs for overlays | Creates extra pages on full-page content | Anchor to existing paragraph |
| Don't assume calendar grid math transfers | 3×4 and 2×6 grids compute month numbers differently | Recalculate when changing dimensions |

---

## File Lock Handling

If Word/PDF file is open during generation:
1. Stop immediately
2. Inform user which file is locked
3. Wait for user to close the file
4. Retry generation

---

## Project Structure

```
year_planner/
├── CLAUDE.md
├── .claudeignore
├── .markdownlint.json
├── requirements.txt
├── run.bat
├── activate.bat
│
├── .claude/
│   ├── settings.json
│   ├── settings.local.json
│   └── commands/
│       └── save-checkpoint.md
│
├── .vscode/
│   └── settings.json
│
├── assets/
│   └── images/
│
├── backup/
│
├── config/
│   └── config.yaml
│
├── docs/
│   ├── SPEC.md
│   ├── ARCHITECTURE.md
│   └── CHANGELOG.md
│
├── output/
│   ├── year_planner.docx
│   └── year_planner.bak
│
├── scripts/
│   └── check_deps.py
│
├── src/
│   ├── CLAUDE.md
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── document.py
│   ├── sections/
│   │   ├── __init__.py
│   │   ├── backlog.py
│   │   ├── calendar.py
│   │   ├── cover.py
│   │   ├── goals.py
│   │   ├── graph_paper.py
│   │   ├── instructions.py
│   │   ├── monthly.py
│   │   ├── rear_cover.py
│   │   ├── terms_definitions.py
│   │   ├── toc.py
│   │   └── week_planner.py
│   └── utils/
│       ├── __init__.py
│       ├── grid_image.py
│       ├── styles.py
│       └── tables.py
│
└── test/
    ├── CLAUDE.md
    └── print_store_samples/
```
