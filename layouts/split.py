"""Split layout primitive for PyLage Layout."""

from typing import Any

from pylage import Row, Style


DEFAULT_SPLIT_STYLE = Style(
    display="flex",
    flex_direction="row",
    width="100%",
    gap="1rem",
)


def Split(*children: Any, **props: Any):
    """Create a horizontal split layout."""
    style = props.pop("style", None)

    if style is None:
        style = DEFAULT_SPLIT_STYLE

    return Row(
        *children,
        style=style,
        **props,
    )


__all__ = [
    "Split",
    "DEFAULT_SPLIT_STYLE",
]
