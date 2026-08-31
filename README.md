

# pylage_layout

<p align="center">
  <b>A composable layout, theming, and page-template library built on top of PyLage.</b>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-blue.svg">
  <img alt="Build" src="https://img.shields.io/badge/build-passing-brightgreen.svg">
  <img alt="PyPI" src="https://img.shields.io/badge/PyPI-not%20yet%20published-lightgrey.svg">
</p>

---

## Overview

Building dashboards and internal tools in pure Python — with **Streamlit**, **Dash**, **NiceGUI**, or raw **PyLage** — usually means re-solving the same problems over and over:

- Inconsistent spacing, radius, and color values scattered across files
- Manually re-implementing responsive column stacking on every page
- Copy-pasted hero sections, pricing tables, and admin shells with no shared source of truth
- No clean separation between **structure** (layout) and **appearance** (theme)

**`pylage_layout`** solves this by sitting one level above [PyLage](#) as a pure **composition layer**. It does not reinvent PyLage's rendering, state, or styling engine — it composes PyLage primitives into a consistent, responsive, themeable, and reusable layout system, so you can go from "empty page" to "production dashboard" with a handful of high-level Python calls instead of hand-rolled `Row`/`Column` nesting.

> **Design Philosophy:** PyLage owns the engine. `pylage_layout` owns the developer experience.

---

## Key Features

### 🎨 Design Tokens
Single source of truth for visual primitives, validated at runtime:
- `COLORS`, `SPACING`, `RADIUS`, `FONTS`
- `validate_tokens()` guards against missing/incomplete design-system values

### 🌗 Theme Presets
- `LIGHT_THEME` / `DARK_THEME` built via a shared `create_theme()` factory
- `get_theme(name)` / `available_themes()` for runtime theme switching
- Built directly on PyLage's native `Theme` infrastructure — no duplicate theming engine

### 🧱 Core Layout Primitives
| Component | Purpose |
|---|---|
| `Container` | Width-constrained, centered responsive page wrapper |
| `Stack` | Responsive vertical/horizontal stack |
| `Section` | Full-width vertical page section |
| `Center` | Centers children both axes |
| `Split` | Two-pane responsive split layout |
| `TwoColumn` / `ThreeColumn` | Responsive multi-column layouts |
| `SidebarLayout` | Fixed sidebar + fluid content area |

### 🧭 Navigation & Application Shells
| Component | Purpose |
|---|---|
| `AppShell` | Header + Sidebar + Content composition |
| `Header` / `Footer` | Semantic page chrome |
| `Navbar` / `Topbar` | High-level navigation bars over PyLage `Navigation` |
| `NavigationDrawer` / `MobileSidebar` | Responsive drawer-based navigation |
| `TabLayout`, `PaginationLayout`, `MenuLayout`, `BreadcrumbTrail` | Navigation controls |

### 📐 Responsive Helpers
- Every public layout ships with a `DEFAULT_*_STYLE` built on PyLage's `ResponsiveStyle`
- Consistent responsive contract across the whole library:
  - `base` → mobile-first, `flex_direction="column"`
  - `md` → `flex_direction="row"`
  - `lg` → `gap="2rem"`
- Fully overridable via `style=...` on any layout without duplicate-keyword errors (regression-tested)

### 🧩 Reusable UI Patterns
`Hero`, `FeatureSection`, `CTA`, `StatsSection`, `PricingSection`, `ContentSection`, `FAQ`, `Testimonial`, `ContactSection`, `NewsletterSection`, `SearchBar`, `List`, `LoginForm` / `SignupForm`, `EmptyState`, `ErrorState`, `Loading`

### 📄 Complete Page Templates
`LandingPage`, `Dashboard`, `AdminPanel`, `Authentication`, `ProfilePage`, `SettingsPage`, `Documentation` — full pages composed from tokens + themes + layouts + patterns.

---

## Installation

### Requirements
- Python **3.10+**
- [PyLage](#) installed as the underlying rendering framework

### Install directly from GitHub

```bash
pip install git+https://github.com/<your-org>/pylage_layout.git
```

### Local editable install (for development / contribution)

```bash
git clone https://github.com/<your-org>/pylage_layout.git
cd pylage_layout
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -e .
```

---

## Quick Start

```python
import pylage as pl
from pylage import ResponsiveStyle, Style

from pylage_layout.layouts import AppShell, Container, TwoColumn
from pylage_layout.patterns import Hero, FeatureSection, CTA
from pylage_layout.templates import LandingPage
from pylage_layout.themes import get_theme

# 1. Pick a theme
theme = get_theme("dark")

# 2. Define a custom responsive contract for a section
custom_columns_style = ResponsiveStyle(
    base=Style(width="100%", flex_direction="column", gap="1rem"),
    md=Style(flex_direction="row"),
    lg=Style(gap="3rem"),
)

# 3. Compose reusable patterns
hero = Hero(
    title="Build dashboards without fighting layout",
    description="pylage_layout gives you responsive, themeable building blocks.",
    actions=["Get Started", "View Docs"],
)

features = FeatureSection(
    {"title": "Design Tokens", "description": "Consistent spacing, color, and radius."},
    {"title": "Responsive by Default", "description": "Mobile-first ResponsiveStyle everywhere."},
    {"title": "Composable Templates", "description": "Full pages in a few lines of Python."},
    title="Why pylage_layout?",
)

cta = CTA(
    title="Ready to ship faster?",
    description="Install pylage_layout and start composing.",
    actions=["Install Now"],
)

# 4. Assemble a full landing page
page = LandingPage(
    hero=hero,
    features=features,
    cta=cta,
)

# 5. Or build a custom shell with an app-level layout
columns = TwoColumn(
    Container(pl.Text("Left panel")),
    Container(pl.Text("Right panel")),
    style=custom_columns_style,
)

app = AppShell(
    header=pl.Text("My Dashboard"),
    sidebar=pl.Text("Navigation"),
    content=columns,
)

if __name__ == "__main__":
    pl.run(
        app,
        title="pylage_layout Demo",
        output="index.html",
        serve=True,
        open_browser=True,
    )
```

---

## Testing

The full regression suite lives under `tests/` and uses **pytest**. It covers construction, props, children, rendering, theming, responsive behavior, composition, and known regressions — without duplicating PyLage's own framework tests.

### Run the full suite

```bash
pip install pytest
pytest
```

### Run a specific audit

```bash
# Design tokens
pytest tests/test_01_tokens_audit.py

# Layout primitives
pytest tests/test_02_layouts_audit.py tests/test_03_layouts_audit.py

# Reusable patterns
pytest tests/test_04_patterns_audit.py tests/test_05_patterns_audit.py

# Page templates
pytest tests/test_06_templates_audit.py

# Public API surface & package audit
pytest tests/test_00_package_audit.py tests/test_08_public_api_audit.py

# Full master regression (Phases 1–7)
pytest tests/test_all_phases.py
```

### Run with verbose output

```bash
pytest -v
```

---

## Architectural Roadmap

`pylage_layout` is developed in locked, sequential phases, tracked in [`BLUEPRINT.md`](./BLUEPRINT.md), the single source of truth for architecture, status, and rules.




PyLage (framework)
└── pylage_layout (composition layer)
├── tokens/ → design tokens
├── themes/ → theme presets
├── layouts/ → structural primitives & shells
├── patterns/ → reusable UI compositions
├── templates/ → complete page templates
└── tests/ → behavior-focused regression suite


### Master Checklist

| Phase | Scope | Status |
|---|---|---|
| 0 | Foundation — capability audit, boundaries, architecture, API/testing/docs rules | ✅ Complete |
| 1 | Design Tokens — colors, spacing, radius, fonts | ✅ Complete |
| 2 | Theme Presets — Light, Dark (Neutral planned) | ✅ Complete |
| 3 | Core & Multi-area Layouts — `Container`, `Stack`, `Section`, `Center`, `Split`, `TwoColumn`, `ThreeColumn`, `SidebarLayout` | ✅ Complete |
| 3C | Application Layouts — `AppShell`, `Header`, `Footer` | ✅ Complete |
| 4 | Navigation — `Navbar`, `Topbar`, `NavigationDrawer`, `MobileSidebar`, `BreadcrumbTrail`, `TabLayout`, `PaginationLayout` | ✅ Complete |
| 5 | Reusable UI Patterns — Hero, Feature, CTA, Stats, Pricing, FAQ, Testimonial, Contact, States | ✅ Complete |
| 6 | Page Templates — Landing, Dashboard, Admin, Auth, Profile, Settings, Documentation | ✅ Complete |
| 7 | Responsive Design — `ResponsiveStyle` contract across all public layouts | ✅ Complete |
| 8 | Public API — simple, composable, Pythonic surface | ⏳ In Progress |
| 9 | Testing — full behavioral regression coverage | ⏳ In Progress |
| 10 | Documentation — per-feature docs and demo app | ⏳ In Progress |
| 11 | Release — packaging, README, changelog, PyPI | ⏳ In Progress |

### Core Development Rules

1. **PyLage First** — always check for an existing PyLage capability before building.
2. **No Duplication** — never rebuild PyLage's rendering, state, diff, or responsive engines.
3. **Composition Over Reinvention** — prefer composing existing primitives.
4. **Tokens Over Hard-coded Values** — every visual value flows from `tokens/`.
5. **Layout ≠ Theme** — structure and appearance stay strictly separate.
6. **Responsive by Default** — every public layout must define a `ResponsiveStyle` contract.
7. **No Premature Abstraction** — patterns must solve a genuinely reusable problem.
8. **Tests Before Completion** — rendering successfully is not "done."
9. **Documentation Before Phase Completion** — every public feature needs an example.
10. **Blueprint Is Source of Truth** — all architectural decisions are recorded in `BLUEPRINT.md`.

---

## Contributing

Contributions are welcome! Before opening a PR:

1. Read [`BLUEPRINT.md`](./BLUEPRINT.md) — it is the binding architecture and rules document.
2. Confirm the capability doesn't already exist in PyLage or `pylage_layout`.
3. Add or update tests under `tests/` for any behavioral change (construction, props, children, responsiveness, regressions).
4. Run the full suite locally: `pytest`.
5. Keep structural changes documented in `BLUEPRINT.md` — no silent architecture changes.

Please open an issue first for significant API or structural proposals so they can be evaluated against the locked project architecture.

## License

Distributed under the **MIT License**. See `LICENSE` for more information.