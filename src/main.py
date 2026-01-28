"""
Year Planner Generator - Main Entry Point

Generates a configurable Year Planner Microsoft Word document
from a YAML configuration file.

Usage:
    python src/main.py --config config/config.yaml --output output/year_planner.docx
"""

import argparse
import io
import shutil
import sys
from pathlib import Path

from docx2pdf import convert as convert_to_pdf

# Configure stdout for UTF-8 encoding to support box-drawing characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.config import load_config, Config
from src.document import create_document, add_page_break, add_section_break, add_numbered_section_break, add_non_numbered_section_break
from src.sections.cover import generate_cover_page
from src.sections.instructions import generate_instructions_page
from src.sections.calendar import generate_calendar_section
from src.sections.toc import generate_toc
from src.sections.goals import generate_goals_page
from src.sections.week_planner import generate_week_planner
from src.sections.backlog import generate_backlog
from src.sections.graph_paper import generate_graph_paper
from src.sections.monthly import generate_monthly_sections
from src.sections.terms_definitions import generate_terms_definitions
from src.sections.rear_cover import generate_rear_cover

def print_header(program: str, version: str, release: str, author: str) -> None:
    """
    Print the program header box.

    Args:
        program: Program name.
        version: Version number.
        release: Release date.
        author: Author name.
    """
    box_width = 40
    label_width = 8
    # Value width = box_width - (space after │) - label_width - (space after label)
    value_width = box_width - 1 - label_width - 1
    print(f"┌{'─' * box_width}┐")
    print(f"│ {'Program:':<{label_width}} {program:<{value_width}}│")
    print(f"│ {'Version:':<{label_width}} {version:<{value_width}}│")
    print(f"│ {'Release:':<{label_width}} {release:<{value_width}}│")
    print(f"│ {'Author:':<{label_width}} {author:<{value_width}}│")
    print(f"└{'─' * box_width}┘")
    print()


def print_usage() -> None:
    """Print usage instructions."""
    print("Usage:")
    print("  python src/main.py [options]")
    print()
    print("Options:")
    print("  -c, --config FILE   Path to YAML configuration file")
    print("                      (default: config/config.yaml)")
    print("  -o, --output FILE   Output path for generated document")
    print("                      (default: output/year_planner.docx)")
    print("  -h, --help          Show this help message and exit")
    print()


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        description="Generate a Year Planner Word document"
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        default="config/config.yaml",
        help="Path to YAML configuration file (default: config/config.yaml)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="output/year_planner.docx",
        help="Output path for generated document (default: output/year_planner.docx)"
    )
    return parser.parse_args()


def backup_existing_file(output_path: Path) -> None:
    """
    Backup existing output file by renaming to .bak extension.

    Args:
        output_path: Path to the output file.
    """
    if output_path.exists():
        backup_path = output_path.with_suffix('.bak')
        shutil.move(str(output_path), str(backup_path))
        print(f"  Backed up existing file to: {backup_path}")


def generate_year_planner(config: Config, output_path: str) -> None:
    """
    Generate the Year Planner document.

    Args:
        config: Loaded configuration object.
        output_path: Path where the document will be saved.
    """
    print(f"Creating Year Planner for {config.document.year}...")

    # Ensure output directory exists
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Backup existing file if present
    backup_existing_file(output_path)

    # Create document with configured page settings
    document = create_document(config)

    # Generate sections
    print("  Generating cover page...")
    generate_cover_page(document, config)

    # Start new section for main content
    # (Separate section allows different header/footer configuration)
    add_section_break(document, config)
    print("  Generating instructions page...")
    generate_instructions_page(document, config)

    # Calendar section (current year + next year)
    # No page break needed - instructions.py already ends on verso
    print("  Generating calendar pages...")
    generate_calendar_section(document, config)

    # Table of Contents (non-numbered section)
    add_page_break(document)
    print("  Generating table of contents...")
    generate_toc(document, config)

    # Goals page - start new section with page numbering
    # (Section break creates new page, so no separate page break needed)
    add_numbered_section_break(document, config, start_number=1)
    print("  Generating goals page...")
    generate_goals_page(document, config)

    # Backlog section (use minimized page break for precise table fitting)
    add_page_break(document, minimize_height=True)
    print("  Generating backlog...")
    generate_backlog(document, config)

    # Week Planner (use minimized page break for precise table fitting)
    add_page_break(document, minimize_height=True)
    print("  Generating week planner...")
    generate_week_planner(document, config)

    # Monthly sections (12 months with cover pages)
    add_page_break(document)
    print("  Generating monthly sections...")
    generate_monthly_sections(document, config)

    # Terms and Definitions section (use minimized page break for precise table fitting)
    add_page_break(document, minimize_height=True)
    print("  Generating terms and definitions...")
    generate_terms_definitions(document, config)

    # Graph paper section (use minimized page break for precise table fitting)
    add_page_break(document, minimize_height=True)
    print("  Generating graph paper...")
    generate_graph_paper(document, config)

    # Rear cover (inside: blank, outside: blank)
    # Add non-numbered section break to remove page numbers from rear cover
    add_non_numbered_section_break(document, config)
    print("  Generating rear cover...")
    generate_rear_cover(document, config)
    print()

    # Save Word document
    document.save(output_path)
    print(f"Year Planner saved to: {output_path}")

    # Convert to PDF
    pdf_path = output_path.with_suffix('.pdf')
    print(f"Converting to PDF...")
    convert_to_pdf(str(output_path), str(pdf_path))
    print(f"PDF saved to: {pdf_path}")
    print()


def main() -> int:
    """
    Main entry point.

    Returns:
        Exit code (0 for success, non-zero for error).
    """
    args = parse_args()

    try:
        # Load configuration
        config = load_config(args.config)

        # Get document generator metadata from config
        generator_meta = config.raw.get('document_generator', {})
        program = generator_meta.get('program', 'Year Planner Generator')
        version = generator_meta.get('version', '1.0')
        release = generator_meta.get('release', 'Unknown')
        author = generator_meta.get('author', 'Unknown')

        # Print program header and usage
        print_header(program, version, release, author)
        print_usage()

        print(f"Loading configuration from: {args.config}")
        print(f"  ├─ Title:   {config.document.title}")
        print(f"  ├─ Year:    {config.document.year}")
        print(f"  └─ Version: {config.document.version}")
        print()

        # Generate document
        generate_year_planner(config, args.output)

        print("Done!")
        print()
        return 0

    except FileNotFoundError as e:
        print(f"Error: Configuration file not found: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
