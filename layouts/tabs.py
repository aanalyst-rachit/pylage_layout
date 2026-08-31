"""Tab navigation layout for PyLage Layout."""

from typing import Any

from pylage import components


def _component(name: str, *children: Any, **props: Any):
    factory = getattr(components, name, None)
    if factory is None:
        raise RuntimeError(f"PyLage component {name!r} is not available")
    return factory(*children, **props)


def TabsLayout(*children: Any, **props: Any):
    """Create a tabbed layout using PyLage's Tabs primitive."""
    return _component("Tabs", *children, **props)


__all__ = ["TabsLayout"]
