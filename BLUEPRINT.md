# PyLage Layout Blueprint

## 1. Purpose

`pylage_layout` is a higher-level layout, theme, pattern, and page-template library built on top of `PyLage`.

PyLage remains the underlying framework.

`pylage_layout` must reuse PyLage capabilities instead of rebuilding them.

---

# 2. Architecture Boundary


PyLage
├── Components
├── Layout primitives
├── Styling
├── Theme system
├── Responsive system
├── State / Reactivity
├── Registry
└── Runtime
        │
        ▼
pylage_layout
├── tokens/
├── themes/
├── layouts/
├── patterns/
├── templates/
└── tests/


## PyLage owns

* UI primitives
* Components
* State
* Reactivity
* Rendering
* Diff/Patch
* Registry
* Runtime
* Style
* ResponsiveStyle
* Theme infrastructure

## pylage_layout owns

* Design tokens
* Theme presets
* High-level layouts
* Layout compositions
* Reusable UI patterns
* Complete page templates
* Developer-friendly layout APIs
* Documentation
* Tests for its own functionality

---

# 3. Strict Non-Duplication Rule

Before creating anything:

1. Check PyLage.
2. Confirm whether the capability already exists.
3. Reuse the existing PyLage capability.
4. Only build the missing higher-level composition.

Never create a duplicate:

* Button engine
* Card engine
* Grid engine
* Row engine
* Column engine
* State engine
* Reactive engine
* Rendering engine
* Diff engine
* Patch engine
* Responsive engine
* Theme engine
* Registry engine

---

# 4. Locked Project Structure

pylage_layout/
├── tokens/
│   ├── colors.py
│   ├── spacing.py
│   ├── typography.py
│   ├── radius.py
│   ├── shadows.py
│   └── sizing.py
│
├── themes/
│   ├── light.py
│   ├── dark.py
│   ├── neutral.py
│   └── ...
│
├── layouts/
│   ├── page.py
│   ├── container.py
│   ├── section.py
│   ├── stack.py
│   ├── split.py
│   ├── columns.py
│   ├── sidebar.py
│   ├── app_shell.py
│   ├── header.py
│   └── footer.py
│
├── patterns/
│   ├── hero.py
│   ├── feature.py
│   ├── cta.py
│   ├── stats.py
│   ├── pricing.py
│   ├── faq.py
│   ├── testimonial.py
│   ├── contact.py
│   ├── empty_state.py
│   ├── loading_state.py
│   └── error_state.py
│
├── templates/
│   ├── landing.py
│   ├── dashboard.py
│   ├── admin.py
│   ├── auth.py
│   ├── profile.py
│   ├── settings.py
│   └── documentation.py
│
├── tests/
│
└── app/
    ├── layout.py
    └── main.py

This structure is locked.

Any structural change must be documented in this file before implementation.

---

# 5. Phase 0 — Foundation

## 0A — PyLage Capability Audit

Status: COMPLETE

PyLage is the underlying framework and existing capabilities must be reused.

## 0B — Responsibility Boundary

Status: COMPLETE

`pylage_layout` is a composition/layout/theme layer above PyLage.

## 0C — Package Architecture

Status: IN PROGRESS

The target directory structure is defined above.

## 0D — Public API Rules

Status: NOT STARTED

## 0E — Testing Rules

Status: NOT STARTED

## 0F — Documentation Rules

Status: NOT STARTED

### Phase 0 Goal

Lock the architecture and development rules before implementation.

---

# 6. Phase 1 — Design Tokens

Create the visual foundation.

## 1A — Colors

Semantic tokens:

* background
* surface
* surface_alt
* text
* text_muted
* border
* primary
* secondary
* success
* warning
* danger
* info

## 1B — Spacing

Create a consistent spacing scale.

## 1C — Typography

Define:

* font family
* font sizes
* font weights
* line heights

## 1D — Radius

Define reusable radius values.

## 1E — Shadows

Define reusable shadow levels.

## 1F — Sizing

Define reusable:

* container widths
* control heights
* icon sizes
* layout sizes

### Phase 1 completion

All design-system values must have a clear source of truth.

---

# 7. Phase 2 — Theme Presets

PyLage already provides the Theme infrastructure.

We create theme presets.

## 2A

Light Theme

## 2B

Dark Theme

## 2C

Neutral Theme

## 2D

Theme Contract

Every theme must provide the required semantic design tokens.

Theme
├── colors
├── spacing
├── typography
├── radius
├── shadows
└── sizing

## 2E

Theme compatibility testing.

Every public layout should work with Light and Dark themes.

---

# 8. Phase 3 — Core Layout Compositions

These are high-level compositions built using PyLage.

## 3A — Basic

* Page
* Container
* Section
* Stack
* Center

## 3B — Multi-area

* Split
* TwoColumn
* ThreeColumn
* SidebarLayout

## 3C — Application

* AppShell
* HeaderLayout
* FooterLayout

Every layout must define:

* purpose
* API
* children/content
* default structure
* responsive behavior
* theme behavior

---

# 9. Phase 4 — Navigation Compositions

Use PyLage navigation capabilities.

## 4A

* Navbar
* Topbar

## 4B

* Sidebar
* MobileSidebar
* NavigationDrawer

## 4C

* BreadcrumbLayout
* TabLayout
* PaginationLayout

No separate navigation engine.

---

# 10. Phase 5 — Reusable UI Patterns

Patterns combine existing PyLage components with `pylage_layout` layouts.

## Marketing

* Hero
* FeatureSection
* CTA
* StatsSection
* PricingSection

## Content

* ContentSection
* FAQ
* Testimonial
* ContactSection

## State

* EmptyState
* LoadingState
* ErrorState

A pattern must solve a reusable composition problem.

Single-use UI must not automatically become a pattern.

---

# 11. Phase 6 — Page Templates

Complete page-level compositions.

## 6A

Landing Page

## 6B

Dashboard

## 6C

Admin Panel

## 6D

Authentication

## 6E

Profile

## 6F

Settings

## 6G

Documentation

Templates must be compositions of:

PyLage
+
tokens
+
themes
+
layouts
+
patterns

---

# 12. Phase 7 — Responsive Design

PyLage's existing responsive system must be reused.

Every public layout must explicitly define:

* Desktop
* Tablet
* Mobile

Responsive behavior must be designed during implementation.

It must not be added as a final patch.

---

# 13. Phase 8 — Public API

The API must be:

* simple
* composable
* predictable
* Pythonic

Target usage:

```python
from pylage_layout.layouts import AppShell

app = AppShell(
    header=...,
    sidebar=...,
    content=...
)
```

Example pattern:

```python
from pylage_layout.patterns import Hero

hero = Hero(
    title="Build with Python",
    description="...",
    actions=[...],
)
```

---

# 14. Phase 9 — Testing

Every public feature must have tests.

Test:

* construction
* props
* children
* rendering
* themes
* responsive behavior
* composition
* regression cases

Do not duplicate PyLage's framework tests.

Only test behavior introduced by `pylage_layout`.

---

# 15. Phase 10 — Documentation

Every public feature requires:

* purpose
* API
* example
* theme behavior
* responsive behavior

The demo application must consume the library.

The demo must not become the library implementation.

---

# 16. Phase 11 — Release

Release requirements:

* package metadata
* README
* examples
* documentation
* tests
* version
* changelog
* PyPI-ready package

---

# 17. Strict Development Rules

## Rule 1 — PyLage First

Always inspect PyLage before implementation.

## Rule 2 — No Duplication

Existing PyLage functionality must be reused.

## Rule 3 — Composition Over Reinvention

Prefer composing existing PyLage capabilities.

## Rule 4 — Tokens Over Repeated Values

Do not repeatedly hard-code design-system values.

## Rule 5 — Theme and Structure Are Separate

Layout = structure
Theme = appearance

## Rule 6 — Responsive by Default

Every public layout must support responsive behavior.

## Rule 7 — No Premature Abstraction

Only create reusable abstractions with a clear purpose.

## Rule 8 — Do Not Modify PyLage Without Proof

A PyLage change requires:

1. confirmed limitation/bug
2. investigation
3. documented reason
4. decision about correct ownership

## Rule 9 — Tests Before Completion

A feature is not complete merely because it renders.

## Rule 10 — Documentation Before Phase Completion

A public feature requires an example and documentation.

## Rule 11 — One Phase at a Time

Do not randomly jump between phases.

## Rule 12 — Blueprint Is Source of Truth

Architecture, roadmap, rules, and major decisions are recorded here.

## Rule 13 — No Silent Architecture Changes

Any architecture change must document:

What changed
Why
Impact
Decision

## Rule 14 — No Workarounds Before Investigation

Unexpected PyLage behavior must be investigated in PyLage before adding a workaround.

## Rule 15 — Demo Is Not Library Code

`app/` demonstrates the library.

It must not contain functionality that belongs inside the package.

---

# 18. Current Status

Phase 0   ████████░░  80%
Phase 1   ░░░░░░░░░░   0%
Phase 2   ░░░░░░░░░░   0%
Phase 3   ░░░░░░░░░░   0%
Phase 4   ░░░░░░░░░░   0%
Phase 5   ░░░░░░░░░░   0%
Phase 6   ░░░░░░░░░░   0%
Phase 7   ░░░░░░░░░░   0%
Phase 8   ░░░░░░░░░░   0%
Phase 9   ░░░░░░░░░░   0%
Phase 10  ░░░░░░░░░░   0%
Phase 11  ░░░░░░░░░░   0%

Current implementation is still at the initial demo stage.

The demo proves that PyLage can already be composed into a page.

The reusable `pylage_layout` system is not yet implemented.

---

# 19. Current Next Step

Do not start building random layouts.

First complete:

Phase 0D — Public API Rules
Phase 0E — Testing Rules
Phase 0F — Documentation Rules

Then begin:

Phase 1 — Design Tokens


---

# 20. Core Principle

PyLage
    =
Framework

pylage_layout
    =
Design Tokens
+
Theme Presets
+
Layout Compositions
+
UI Patterns
+
Page Templates

The objective is to make complete UI development with PyLage faster, reusable, consistent, responsive, and themeable.

`pylage_layout` extends PyLage through composition.

It does not replace PyLage.
It does not duplicate PyLage.