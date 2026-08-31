"""Stack layout primitive for PyLage Layout."""

from typing import Any

from pylage import Column, Style


DEFAULT_STACK_STYLE = Style(
    display="flex",
    flex_direction="column",
    width="100%",
    gap="1rem",
)


def Stack(*children: Any, **props: Any):
    """Create a vertical stack with consistent spacing."""
    style = props.pop("style", None)

    if style is None:
        style = DEFAULT_STACK_STYLE

    return Column(
        *children,
        style=style,
        **props,
    )


__all__ = [
    "Stack",
    "DEFAULT_STACK_STYLE",
]
