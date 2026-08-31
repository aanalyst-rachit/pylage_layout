"""Two-column layout primitive for PyLage Layout."""

from typing import Any

from pylage import Row, Style


DEFAULT_TWO_COLUMN_STYLE = Style(
    display="flex",
    flex_direction="row",
    width="100%",
    gap="1rem",
)


def TwoColumn(*children: Any, **props: Any):
    """Create a two-column horizontal layout."""
    style = props.pop("style", None)

    if style is None:
        style = DEFAULT_TWO_COLUMN_STYLE

    return Row(
        *children,
        style=style,
        **props,
    )


__all__ = [
    "TwoColumn",
    "DEFAULT_TWO_COLUMN_STYLE",
]
