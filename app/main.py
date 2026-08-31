import pylage as pl

from layouts.layout import build_layout


app = build_layout()

if __name__ == "__main__":
    pl.run(
        app,
        title="PyLage Layout Demo",
        output="index.html",
        serve=True,
        open_browser=True,
    )