from textual.app import App, ComposeResult

from textualeffects.effects import EffectType
from textualeffects.widgets import EffectLabel

text = ("Hello World! " * 5 + "\n") * 10
effect: EffectType = "Spotlights"
config = {
    "search_duration": 500,
    "spotlight_count": 3,
}


class TextualEffect(App):

    def compose(self) -> ComposeResult:
        label = EffectLabel(text, effect=effect, config=config)
        label.styles.border = ("heavy", "green")
        yield label


if __name__ == "__main__":
    app = TextualEffect()
    app.run()
