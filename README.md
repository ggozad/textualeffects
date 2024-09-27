# textualeffects

Visual effects for Textual, a [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) wrapper.

## Intro 

`textualeffects` is a library that provides [Textual](https://textual.textualize.io) bindings for the excellent [TerminalTextEffects](https://github.com/ChrisBuilds/terminaltexteffects) visual effects library.

## Widgets

There are two widgets available in `textualeffects`, `EffectLabel` and `SplashScreen`.

An `EffectLabel` widget that can be used to display text with a visual effect.
```python
from textual.app import App, ComposeResult

from textualeffects.effects import EffectType
from textualeffects.widgets import EffectLabel

text=("Hello World! " * 5 + "\n") * 10,
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

```

![EffectLabel](./screenshots/EffectLabel.gif)

A `SplashScreen` widget that can be used to display a splash screen based on `ModalScreen` with a visual effect. Once the effect is complete, the splash screen will be dismissed. The user can also dismiss the splash screen by pressing the <kbd>ESC</kbd> key.

```python
from textual.app import App, ComposeResult
from textual.widgets import TextArea

from textualeffects.effects import EffectType
from textualeffects.widgets import SplashScreen

effect: EffectType = "Spotlights"
config = {
    "search_duration": 100,
    "spotlight_count": 3,
}


class SplashEffect(App):

    def on_mount(self) -> None:
        text = ("Hello World! " * 5 + "\n") * 10
        self.push_screen(SplashScreen(text, effect=effect, config=config))

    def compose(self) -> ComposeResult:
        yield TextArea(("Main content" * 5 + "\n") * 10)


if __name__ == "__main__":
    app = SplashEffect()
    app.run()
```

![EffectLabel](./screenshots/SplashScreen.gif)

Both widgets accept the following arguments:
- `text`: The text to display.
- `effect`: The visual effect to apply to the text. Available effects are exposed through the `EffectType` type.
- `config`: A dictionary of configuration options for the effect. The available options depend on the effect. Detailed information on the available options can be found in the [TerminalTextEffects documentation](https://chrisbuilds.github.io/terminaltexteffects/showroom/).

For convenience, when an effect has run its course, the `EffectLabel` and `SplashScreen` widgets will emit a `EffectLabel.EffectFinished` event.
You can listen for this event to perform any actions:

```python
    @on(EffectLabel.EffectFinished)
    def do_stuff(self, message: EffectLabel.EffectFinished) -> None:
        ...
```
## License

This project is licensed under the [MIT License](LICENSE).
