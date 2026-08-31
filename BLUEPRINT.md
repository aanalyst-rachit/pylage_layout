# PyLage Layout Blueprint

## Project Progress Summary

### Completed Phases:
- Phase 0A — PyLage Capability Audit: ✅ COMPLETE
- Phase 0B — Responsibility Boundary: ✅ COMPLETE
- Phase 0C — Package Architecture: ✅ COMPLETE
- Phase 3A — Basic Layouts: ✅ PASS (Page, Container, Section, Stack, Center)
- Phase 3B — Multi-area Layouts: ✅ PASS (Split, TwoColumn, ThreeColumn, SidebarLayout)
- Phase 3C — Application Layouts: ✅ PASS (HeaderLayout, FooterLayout)
- Phase 4A — Navigation Components: ✅ PASS (Navbar)
- Phase 4B — Sidebar Components: ✅ PASS (NavigationDrawer)
- Phase 4C — Navigation Layouts: ✅ PASS (BreadcrumbLayout)

### In Progress Phases:
- Phase 0D — Public API Rules:  ✅ COMPLETE
- Phase 0E — Testing Rules:  ✅ COMPLETE
- Phase 0F — Documentation Rules:  ✅ COMPLETE
- Phase 1 — Design Tokens:  ✅ COMPLETE
- Phase 2 — Theme Presets:  ✅ COMPLETE (Light Theme, Dark Theme, Neutral Theme)
- Phase 3C — Application Layouts:  ✅ COMPLETE (AppShell)
- Phase 4A — Navigation Components:  ✅ COMPLETE (Topbar)
- Phase 4B — Sidebar Components: ⏳ IN PROGRESS (Sidebar, MobileSidebar)
- Phase 4C — Navigation Layouts: ✅ COMPLETE (BreadcrumbLayout, TabLayout, PaginationLayout)
- Phase 5 — Reusable UI Patterns:  ✅ COMPLETE (All patterns)
- Phase 6 — Page Templates: ✅ COMPLETE (Landing, Dashboard, Admin, Authentication, Profile, Settings, Documentation)
- Phase 7 — Responsive Design: ✅ COMPLETE
- Phase 8 — Public API: ⏳ IN PROGRESS
- Phase 9 — Testing: ⏳ IN PROGRESS
- Phase 10 — Documentation: ⏳ IN PROGRESS
- Phase 11 — Release: ⏳ IN PROGRESS

### Total Progress:
- Total Phases: 17
- Completed Phases: 12
- In Progress Phases: 5
- Pending Phases: 0

---

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

Status: ✅ COMPLETE

PyLage is the underlying framework and existing capabilities must be reused.

## 0B — Responsibility Boundary

Status: ✅ COMPLETE

`pylage_layout` is a composition/layout/theme layer above PyLage.

## 0C — Package Architecture

Status: ✅ COMPLETE

The target directory structure is defined above.

## 0D — Public API Rules

Status: ✅ COMPLETE

## 0E — Testing Rules

Status: ✅ COMPLETE

## 0F — Documentation Rules

Status: ✅ COMPLETE

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

## 2A — Light Theme

Status: ⏳ IN PROGRESS

## 2B — Dark Theme

Status: ⏳ IN PROGRESS

## 2C — Neutral Theme

Status: ⏳ IN PROGRESS

## 2D — Theme Contract

Every theme must provide the required semantic design tokens.

Theme
├── colors
├── spacing
├── typography
├── radius
├── shadows
└── sizing

## 2E — Theme compatibility testing.

Every public layout should work with Light and Dark themes.

---

# 8. Phase 3 — Core Layout Compositions

These are high-level compositions built using PyLage.

## 3A — Basic Layouts

* Page: ✅ PASS
* Container: ✅ PASS
* Section: ✅ PASS
* Stack: ✅ PASS
* Center: ✅ PASS

## 3B — Multi-area Layouts

* Split: ✅ PASS
* TwoColumn: ✅ PASS
* ThreeColumn: ✅ PASS
* SidebarLayout: ✅ PASS

## 3C — Application Layouts

* AppShell: ✅ PASS
* HeaderLayout: ✅ PASS
* FooterLayout: ✅ PASS

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

## 4A — Navigation Components

* Navbar: ✅ PASS
* Topbar: ✅ PASS

## 4B — Sidebar Components

* Sidebar: ⏳ IN PROGRESS (future tech)
* MobileSidebar: ⏳ IN PROGRESS (future tech)
* NavigationDrawer: ✅ PASS

## 4C — Navigation Layouts

* BreadcrumbLayout: ✅ PASS
* TabLayout: ✅ PASS
* PaginationLayout: ✅ PASS

No separate navigation engine.

---

# 10. Phase 5 — Reusable UI Patterns

Patterns combine existing PyLage components with `pylage_layout` layouts.

## Marketing

* Hero: ✅ PASS
* FeatureSection: ✅ PASS
* CTA: ✅ PASS
* StatsSection: ✅ PASS
* PricingSection: ✅ PASS

## Content

* ContentSection: ✅ PASS
* FAQ: ✅ PASS
* Testimonial: ✅ PASS
* ContactSection: ✅ PASS

## State

* EmptyState: ✅ PASS
* LoadingState: ✅ PASS
* ErrorState: ✅ PASS

A pattern must solve a reusable composition problem.

Single-use UI must not automatically become a pattern.

---

# 11. Phase 6 — Page Templates

Complete page-level compositions.

## 6A — Landing Page

Status: ✅ PASS

## 6B — Dashboard

Status: ✅ PASS

## 6C — Admin Panel

Status: ✅ PASS

## 6D — Authentication

Status: ✅ PASS

## 6E — Profile

Status: ✅ PASS

## 6F — Settings

Status: ✅ PASS

## 6G — Documentation

Status: ✅ PASS

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

Phase 7 is responsible for making public `pylage_layout` layouts responsive
through composition with PyLage's existing `ResponsiveStyle` capability.

## 7A — PyLage Responsive Capability Audit

Status: ✅ PASS

Confirmed PyLage provides:

* `ResponsiveStyle`
* `Style`
* `sm` breakpoint at `640px`
* `md` breakpoint at `768px`
* `lg` breakpoint at `1024px`
* `xl` breakpoint at `1280px`

PyLage owns the responsive engine.

`pylage_layout` must not create a duplicate responsive engine.

## 7B — Existing Layout Responsive Audit

Status: ✅ COMPLETE

Existing layouts were audited for responsive capability.

Findings:

* Most layouts currently use static `Style` definitions.
* `NavigationDrawer` / `MobileSidebar` reuse PyLage's responsive-capable Drawer.
* `ThreeColumn` currently has a responsive-oriented composition but does not
  yet explicitly use `ResponsiveStyle`.
* `SidebarLayout` currently uses fixed sidebar sizing and requires responsive
  behavior.
* Container, Stack, Split, TwoColumn, Header, Footer, Navbar and Topbar
  require explicit responsive contracts where applicable.

## 7C — Responsive Layout Contract

Status: ✅ COMPLETE

Every public layout that requires responsive behavior must define:

* Mobile/base behavior
* Tablet behavior where required
* Desktop behavior where required
* Breakpoint-specific overrides using PyLage `ResponsiveStyle`
* Stable layout structure across breakpoints
* No duplicated responsive engine

Responsive behavior must be implemented using PyLage primitives.

## 7D — Core Layout Responsiveness

Status:  ✅ COMPLETE

Audit and implement responsive behavior for:

* Container
* Stack
* Split
* TwoColumn
* ThreeColumn
* SidebarLayout

## 7E — Navigation Responsiveness

Status: ✅ COMPLETE

Audit and implement responsive behavior for:

* Navbar
* Topbar
* Header
* Footer
* NavigationDrawer
* MobileSidebar

## 7F — Responsive Composition Tests

Status: ✅ COMPLETE

Test:

* responsive style construction
* breakpoint overrides
* mobile behavior
* tablet behavior
* desktop behavior
* layout composition
* regression cases

Tests must verify behavior introduced by `pylage_layout`, not duplicate
PyLage framework tests.

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

Phase 0   ✅ COMPLETE
Phase 1   ⏳ IN PROGRESS
Phase 2   ⏳ IN PROGRESS
Phase 3   ⏳ IN PROGRESS
Phase 4   ⏳ IN PROGRESS
Phase 5   ⏳ IN PROGRESS
Phase 6   ⏳ IN PROGRESS
Phase 7   ⏳ IN PROGRESS
Phase 8   ⏳ IN PROGRESS
Phase 9   ⏳ IN PROGRESS
Phase 10  ⏳ IN PROGRESS
Phase 11  ⏳ IN PROGRESS

Current implementation is still at the initial demo stage.

The demo proves that PyLage can already be composed into a page.

The reusable `pylage_layout` system is not yet implemented.

---

# 19. Current Next Step

Phase 6 page templates are complete.

Phase 7 has now started.

Completed:

* Phase 7A — PyLage Responsive Capability Audit
* Phase 7B — Existing Layout Responsive Audit

Current step:

* Phase 7C — Responsive Layout Contract

After the contract is locked:

* Phase 7D — Core Layout Responsiveness
* Phase 7E — Navigation Responsiveness
* Phase 7F — Responsive Composition Tests

Do not create a new responsive engine.

Reuse PyLage `ResponsiveStyle`.

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