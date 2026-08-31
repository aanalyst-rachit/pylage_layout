"""Validation helpers for PyLage Layout design tokens."""

from collections.abc import Mapping

REQUIRED_COLOR_TOKENS = {
    "background",
    "surface",
    "surface_alt",
    "text",
    "text_muted",
    "border",
    "primary",
    "secondary",
    "success",
    "warning",
    "danger",
    "info",
}

REQUIRED_SPACING_TOKENS = {
    "0",
    "xs",
    "sm",
    "md",
    "lg",
    "xl",
    "2xl",
    "3xl",
    "4xl",
}

REQUIRED_RADIUS_TOKENS = {
    "none",
    "sm",
    "md",
    "lg",
    "xl",
    "2xl",
    "full",
}

REQUIRED_FONT_TOKENS = {
    "sans",
    "serif",
    "mono",
}


def validate_tokens(
    *,
    colors: Mapping[str, object],
    spacing: Mapping[str, object],
    radius: Mapping[str, object],
    fonts: Mapping[str, object],
) -> None:
    """Validate that all required design tokens are present."""
    _validate_section("colors", colors, REQUIRED_COLOR_TOKENS)
    _validate_section("spacing", spacing, REQUIRED_SPACING_TOKENS)
    _validate_section("radius", radius, REQUIRED_RADIUS_TOKENS)
    _validate_section("fonts", fonts, REQUIRED_FONT_TOKENS)


def _validate_section(
    section: str,
    values: Mapping[str, object],
    required: set[str],
) -> None:
    missing = required - set(values)

    if missing:
        names = ", ".join(sorted(missing))
        raise ValueError(
            f"Missing {section} token(s): {names}"
        )


__all__ = [
    "REQUIRED_COLOR_TOKENS",
    "REQUIRED_FONT_TOKENS",
    "REQUIRED_RADIUS_TOKENS",
    "REQUIRED_SPACING_TOKENS",
    "validate_tokens",
]
