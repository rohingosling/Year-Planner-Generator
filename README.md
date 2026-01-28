# Year Planner Generator

A Python application that generates a configurable, printable Year Planner as a Microsoft Word document, optimized for duplex printing.

## Features

- **Configurable layout** — All dimensions, colors, and row counts controlled via YAML
- **Duplex-ready** — Strict recto/verso page layout with mirror margins and gutter
- **Complete planner sections:**
  - Cover page with contact info
  - Instructions page
  - Year-at-a-glance calendars (current + next year)
  - Table of Contents with pre-calculated page numbers
  - Goals page
  - Backlog section for unscheduled tasks
  - Week Planner with ISO 8601 week numbering
  - Monthly sections with daily spreads (×12)
  - Graph paper pages
- **Automatic PDF export** — Generates both `.docx` and `.pdf`
- **Minimal aesthetic** — Black, white, and grayscale design optimized for print

## Requirements

- Python 3.12+
- Microsoft Word (required for PDF conversion via `docx2pdf`)

## Installation

```bash
# Clone the repository

git clone https://github.com/yourusername/year-planner.git
cd year-planner

# Create virtual environment

python -m venv .venv

# Activate virtual environment
# Windows

.venv\Scripts\activate

# Linux/macOS

source .venv/bin/activate

# Install dependencies

pip install -r requirements.txt
```

## Usage

### Generate Year Planner

```bash
python src/main.py
```

Or on Windows:

```batch
run.bat
```

Output files are saved to `output/`:
- `year_planner.docx` — Editable Word document
- `year_planner.pdf` — Print-ready PDF

### Configuration

Edit `config/config.yaml` to customize:

```yaml
document:
  title:   "Year Planner"
  version: "1.0"
  year:    2026

page:
  width:         21.0    # A4 width (cm)
  height:        29.7    # A4 height (cm)
  margin_top:    0.6
  margin_bottom: 1.2
  margin_left:   0.6
  margin_right:  0.6
  gutter_size:   1.5     # Binding margin (cm)

backlog:
  page_count: 4
  row_count:  16

graph_paper:
  page_count: 8
  columns:    37
  rows:       56
```

See `docs/SPEC.md` for complete configuration reference.

## Project Structure

```
year_planner/
├── config/
│   └── config.yaml      # Generator configuration
├── docs/
│   ├── SPEC.md          # Product specification
│   ├── ARCHITECTURE.md  # System design
│   └── CHANGELOG.md     # Version history
├── output/              # Generated documents
├── src/
│   ├── main.py          # Entry point
│   ├── config.py        # Configuration loading
│   ├── document.py      # Document utilities
│   ├── sections/        # Section generators
│   └── utils/           # Shared helpers
└── assets/
    └── images/          # Generated grid images (cached)
```

## Printing

For best results:

1. Print duplex (two-sided), flip on long edge
2. Use A4 paper
3. Set print scaling to 100% (no fit-to-page)
4. Bind on the left edge

## Documentation

| Document | Description |
|----------|-------------|
| [SPEC.md](docs/SPEC.md) | Complete product specification |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design and implementation details |
| [CHANGELOG.md](docs/CHANGELOG.md) | Version history |
| [BACKLOG.md](docs/BACKLOG.md) | Task tracking and velocity metrics |

## License

MIT

## Author

Rohin Gosling
