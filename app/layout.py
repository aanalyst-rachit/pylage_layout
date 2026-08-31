import pylage as pl


def build_layout():
    header = pl.Row(
        pl.Text("PyLage", style={
            "font-size": "28px",
            "font-weight": "700",
        }),
        pl.Text("Layout Studio", style={
            "font-size": "14px",
            "opacity": "0.7",
        }),
        style={
            "display": "flex",
            "align-items": "center",
            "justify-content": "space-between",
            "padding": "20px 28px",
        },
    )

    hero = pl.Column(
        pl.Text(
            "Build beautiful interfaces with Python",
            style={
                "font-size": "36px",
                "font-weight": "700",
                "margin-bottom": "10px",
            },
        ),
        pl.Text(
            "A modern layout experiment powered by PyLage 1.0.0",
            style={
                "font-size": "16px",
                "opacity": "0.7",
                "margin-bottom": "24px",
            },
        ),
        pl.Row(
            pl.Button(
                "Get Started",
                style={
                    "padding": "12px 20px",
                    "border-radius": "10px",
                    "font-weight": "600",
                },
            ),
            pl.Button(
                "Explore",
                style={
                    "padding": "12px 20px",
                    "border-radius": "10px",
                },
            ),
            style={
                "display": "flex",
                "gap": "12px",
            },
        ),
        style={
            "padding": "48px 28px",
        },
    )

    cards = pl.Row(
        pl.Column(
            pl.Text("01", style={"font-size": "13px", "opacity": "0.6"}),
            pl.Text("Layout", style={"font-size": "22px", "font-weight": "700"}),
            pl.Text("Compose interfaces using simple Python components."),
            style={
                "padding": "24px",
                "border-radius": "16px",
            },
        ),
        pl.Column(
            pl.Text("02", style={"font-size": "13px", "opacity": "0.6"}),
            pl.Text("Styling", style={"font-size": "22px", "font-weight": "700"}),
            pl.Text("Keep visual design close to the components."),
            style={
                "padding": "24px",
                "border-radius": "16px",
            },
        ),
        pl.Column(
            pl.Text("03", style={"font-size": "13px", "opacity": "0.6"}),
            pl.Text("Reactive", style={"font-size": "22px", "font-weight": "700"}),
            pl.Text("Build toward interactive Python applications."),
            style={
                "padding": "24px",
                "border-radius": "16px",
            },
        ),
        style={
            "display": "flex",
            "gap": "16px",
            "padding": "0 28px 28px",
        },
    )

    return pl.Column(
        header,
        hero,
        cards,
        style={
            "min-height": "100vh",
            "font-family": "Inter, system-ui, sans-serif",
            "background": "#f7f8fc",
            "color": "#111827",
        },
    )
