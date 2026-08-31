"""Three-column layout for PyLage Layout."""

from typing import Any

from pylage import Row, Style


def ThreeColumn(*children: Any, **props: Any):
    """Create a responsive three-column layout."""
    class_name = props.pop("class_name", "three-column")

    style = Style(
        display="flex",
        flex_direction="row",
        gap="1rem",
        width="100%",
    )

    return Row(
        *children,
        class_name=class_name,
        style=style,
        **props,
    )


__all__ = ["ThreeColumn"]
