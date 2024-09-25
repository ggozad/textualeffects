from textual.app import App, ComposeResult
from textual.widgets import TextArea

from textualeffects.effects import EffectType
from textualeffects.widgets import SplashScreen

text = ("Hello World! " * 5 + "\n") * 10
effect: EffectType = "Spotlights"
config = {
    "search_duration": 100,
    "spotlight_count": 3,
}


class SplashEffect(App):

    def on_mount(self) -> None:
        self.push_screen(SplashScreen(text, effect=effect, config=config))

    def compose(self) -> ComposeResult:
        yield TextArea(("Main content" * 5 + "\n") * 10)


if __name__ == "__main__":
    app = SplashEffect()
    app.run()
