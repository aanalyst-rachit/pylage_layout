"""Container layout primitive for PyLage Layout."""

from typing import Any

from pylage import Column, Style


DEFAULT_CONTAINER_STYLE = Style(
    max_width="1200px",
    margin="0 auto",
    width="100%",
)


def Container(*children: Any, **props: Any):
    """Create a centered, width-constrained page container."""
    style = props.pop("style", None)

    if style is None:
        style = DEFAULT_CONTAINER_STYLE

    return Column(
        *children,
        style=style,
        **props,
    )


__all__ = [
    "Container",
    "DEFAULT_CONTAINER_STYLE",
]
