"""
Configuration loader for Year Planner generator.

Loads and validates YAML configuration files.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class DocumentConfig:
    """Document metadata configuration."""
    title: str
    version: str
    year: int


@dataclass
class PageConfig:
    """Page layout configuration."""
    width: float
    height: float
    margin_top: float
    margin_bottom: float
    margin_left: float
    margin_right: float
    gutter_size: float
    page_number_position: float


@dataclass
class BorderConfig:
    """Table border configuration."""
    thickness: float   # Line thickness in points
    grayscale: int     # Color (0=white, 100=black)


@dataclass
class TitleRowConfig:
    """Table title row configuration."""
    height: float               # Row height in points
    background_grayscale: int   # Background color (0=white, 100=black)
    font_size: float            # Font size in points
    font_grayscale: int         # Font color (0=white, 100=black)


@dataclass
class HeaderRowConfig:
    """Table header row configuration."""
    height: float               # Row height in points
    background_grayscale: int   # Background color (0=white, 100=black)
    font_size: float            # Font size in points
    font_grayscale: int         # Font color (0=white, 100=black)


@dataclass
class ContentRowConfig:
    """Table content row configuration."""
    font_size: float      # Font size in points
    font_grayscale: int   # Font color (0=white, 100=black)
    font_italic: bool     # Whether content text is italic


@dataclass
class TableConfig:
    """Table styling configuration."""
    border: BorderConfig
    title_row: TitleRowConfig
    header_row: HeaderRowConfig
    content_row: ContentRowConfig


@dataclass
class DebugConfig:
    """Debug mode configuration."""
    enabled: bool
    config_info_overlay: bool


@dataclass
class ConfigInfoOverlayConfig:
    """Configuration info overlay settings."""
    bottom: float           # Distance from bottom edge of page in cm
    right: float            # Distance from right edge (recto pages) in cm
    left: float             # Distance from left edge (verso pages) in cm
    width: float            # Text box width in cm
    title: str              # Overlay title text
    title_font_size: float  # Title text font size in points
    data_font_size: float   # Field data font size in points


@dataclass
class ContactTableConfig:
    """Contact table configuration."""
    row_height: float
    label_width: float
    value_width: float


@dataclass
class CoverConfig:
    """Cover page configuration."""
    contact_fields: list[str]
    contact_table: ContactTableConfig


@dataclass
class Config:
    """Main configuration container."""
    debug: DebugConfig
    config_info_overlay: ConfigInfoOverlayConfig
    document: DocumentConfig
    page: PageConfig
    table: TableConfig
    cover: CoverConfig
    raw: dict[str, Any]  # Store raw config for future sections


def load_config(config_path: str | Path) -> Config:
    """
    Load configuration from a YAML file.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Config object with parsed configuration values.

    Raises:
        FileNotFoundError: If config file doesn't exist.
        yaml.YAMLError: If config file is invalid YAML.
    """
    config_path = Path(config_path)

    with open(config_path, 'r', encoding='utf-8') as f:
        raw = yaml.safe_load(f)

    document = DocumentConfig(
        title=raw['document']['title'],
        version=raw['document']['version'],
        year=raw['document']['year']
    )

    page = PageConfig(
        width=raw['page']['width'],
        height=raw['page']['height'],
        margin_top=raw['page']['margin_top'],
        margin_bottom=raw['page']['margin_bottom'],
        margin_left=raw['page']['margin_left'],
        margin_right=raw['page']['margin_right'],
        gutter_size=raw['page']['gutter_size'],
        page_number_position=raw['page']['page_number_position']
    )

    # Parse table config with nested structures
    table_raw = raw['table']

    border = BorderConfig(
        thickness=table_raw['border']['thickness'],
        grayscale=table_raw['border']['grayscale']
    )

    title_row = TitleRowConfig(
        height=table_raw['title_row']['height'],
        background_grayscale=table_raw['title_row']['background_grayscale'],
        font_size=table_raw['title_row']['font_size'],
        font_grayscale=table_raw['title_row']['font_grayscale']
    )

    header_row = HeaderRowConfig(
        height=table_raw['header_row']['height'],
        background_grayscale=table_raw['header_row']['background_grayscale'],
        font_size=table_raw['header_row']['font_size'],
        font_grayscale=table_raw['header_row']['font_grayscale']
    )

    content_row = ContentRowConfig(
        font_size=table_raw['content_row']['font_size'],
        font_grayscale=table_raw['content_row']['font_grayscale'],
        font_italic=table_raw['content_row']['font_italic']
    )

    table = TableConfig(
        border=border,
        title_row=title_row,
        header_row=header_row,
        content_row=content_row
    )

    contact_table = ContactTableConfig(
        row_height=raw['cover']['contact_table']['row_height'],
        label_width=raw['cover']['contact_table']['label_width'],
        value_width=raw['cover']['contact_table']['value_width']
    )

    cover = CoverConfig(
        contact_fields=raw['cover']['contact_fields'],
        contact_table=contact_table
    )

    # Parse debug config (handle both old boolean and new dict format)
    debug_raw = raw.get('debug', {})
    if isinstance(debug_raw, bool):
        # Backwards compatibility with old format
        debug = DebugConfig(enabled=debug_raw, config_info_overlay=False)
    else:
        debug = DebugConfig(
            enabled=debug_raw.get('enabled', False),
            config_info_overlay=debug_raw.get('config_info_overlay', False)
        )

    # Parse config info overlay settings
    overlay_raw = raw.get('config_info_overlay', {})
    config_info_overlay = ConfigInfoOverlayConfig(
        bottom=overlay_raw.get('bottom', 1.5),
        right=overlay_raw.get('right', 1.5),
        left=overlay_raw.get('left', 1.5),
        width=overlay_raw.get('width', 6.0),
        title=overlay_raw.get('title', 'Config Info'),
        title_font_size=overlay_raw.get('title_font_size', 7),
        data_font_size=overlay_raw.get('data_font_size', 5)
    )

    return Config(
        debug=debug,
        config_info_overlay=config_info_overlay,
        document=document,
        page=page,
        table=table,
        cover=cover,
        raw=raw
    )
