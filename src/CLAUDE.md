# Source Code Guidelines

Context for Claude Code when working in `src/`.

## Module Structure

| Module | Purpose |
|--------|---------|
| `main.py` | Entry point, CLI, PDF conversion |
| `config.py` | YAML loading and validation |
| `document.py` | Document init, page breaks, section breaks, debug visualization |
| `sections/*.py` | Individual document sections |
| `utils/*.py` | Shared helpers (styles, tables, grid images) |

## Key Functions in `document.py`

| Function | Use |
|----------|-----|
| `compute_table_row_height()` | Calculate content row height to fill page |
| `validate_table_height()` | Warn if table won't fit |
| `add_page_break(minimize_height=True)` | Minimal-space page break |
| `add_numbered_section_break()` | Section break with page numbering |
| `add_non_numbered_section_break()` | Section break without footers |
| `get_content_height_twips()` | Available vertical space |
| `get_content_width_twips()` | Available horizontal space |

## Table Row Height Formula

$$r_c = \frac{p_v - p_{para} - s - r_t - r_h}{n}$$

| Symbol | Value |
|--------|-------|
| $p_{para}$ | 20 twips (minimized paragraph) |
| $s$ | 40 twips (safety margin) |
| $r_t$, $r_h$ | From config (default 284 twips each) |

## Section Module Pattern

```python
def add_section(document: Document, config: dict) -> None:
    """Add [Section Name] to document.
    
    Args:
        document: python-docx Document instance
        config: Loaded configuration dict
    """
    # 1. Read config values
    # 2. Add section break if needed
    # 3. Build table(s)
    # 4. Apply styling
```

## Style Conventions

- Use `_` prefix for internal helpers (e.g., `_set_cell_shading()`)
- Constants in UPPER_SNAKE_CASE
- Type hints on all public functions
- Docstrings for public functions (Google format)
