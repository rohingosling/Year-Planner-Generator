"""
Table creation utilities for Year Planner document.

Provides helpers for creating and styling Word tables.
"""

from docx import Document
from docx.table import Table, _Cell
from docx.shared import Cm, Pt, RGBColor
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.enum.table import WD_TABLE_ALIGNMENT

from src.config import TableConfig


def create_table(document: Document, rows: int, cols: int,
                 width: float) -> Table:
    """
    Create a table with specified dimensions.

    Args:
        document: The Word document.
        rows: Number of rows.
        cols: Number of columns.
        width: Table width in centimeters.

    Returns:
        The created table.
    """
    table = document.add_table(rows=rows, cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Set table width
    for row in table.rows:
        for cell in row.cells:
            cell.width = Cm(width / cols)

    return table


def set_table_borders(table: Table, config: TableConfig) -> None:
    """
    Apply border styling to a table.

    Args:
        table: The table to style.
        config: Table configuration with border settings.
    """
    # Calculate grayscale color value (0=white, 100=black)
    gray_value = int(255 * (1 - config.border.grayscale / 100))
    color_hex = f"{gray_value:02X}{gray_value:02X}{gray_value:02X}"

    # Border size in eighths of a point
    border_size = int(config.border.thickness * 8)

    tbl = table._tbl
    tbl_pr = tbl.tblPr if tbl.tblPr is not None else parse_xml(
        r'<w:tblPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'
    )

    tbl_borders = parse_xml(
        f'''<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
            <w:left w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
            <w:bottom w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
            <w:right w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
            <w:insideH w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
            <w:insideV w:val="single" w:sz="{border_size}" w:color="{color_hex}"/>
        </w:tblBorders>'''
    )

    tbl_pr.append(tbl_borders)
    if tbl.tblPr is None:
        tbl.insert(0, tbl_pr)


def remove_table_borders(table: Table) -> None:
    """
    Remove all borders from a table.

    Args:
        table: The table to remove borders from.
    """
    tbl = table._tbl
    tbl_pr = tbl.tblPr if tbl.tblPr is not None else parse_xml(
        r'<w:tblPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'
    )

    tbl_borders = parse_xml(
        '''<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="nil"/>
            <w:left w:val="nil"/>
            <w:bottom w:val="nil"/>
            <w:right w:val="nil"/>
            <w:insideH w:val="nil"/>
            <w:insideV w:val="nil"/>
        </w:tblBorders>'''
    )

    tbl_pr.append(tbl_borders)
    if tbl.tblPr is None:
        tbl.insert(0, tbl_pr)


def set_cell_vertical_alignment(cell: _Cell, alignment: str = "center") -> None:
    """
    Set vertical alignment of a table cell.

    Args:
        cell: The cell to align.
        alignment: Vertical alignment ('top', 'center', 'bottom').
    """
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    val_map = {"top": "top", "center": "center", "bottom": "bottom"}
    v_align = parse_xml(
        f'<w:vAlign xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="{val_map.get(alignment, "center")}"/>'
    )
    tc_pr.append(v_align)


def set_cell_shading(cell: _Cell, grayscale: int) -> None:
    """
    Set the background shading of a table cell using grayscale value.

    Args:
        cell: The cell to shade.
        grayscale: Grayscale percentage (0=white, 100=black).
    """
    # Convert grayscale percentage to hex color
    gray_value = int(255 * (1 - grayscale / 100))
    color_hex = f"{gray_value:02X}{gray_value:02X}{gray_value:02X}"

    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    shd = parse_xml(
        f'<w:shd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        f'w:val="clear" w:color="auto" w:fill="{color_hex}"/>'
    )
    tc_pr.append(shd)
