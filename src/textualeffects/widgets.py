import asyncio
from typing import Any

from rich.text import Text
from terminaltexteffects.engine.base_effect import BaseEffect
from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.message import Message
from textual.reactive import reactive, var
from textual.screen import ModalScreen
from textual.widgets import Static

from textualeffects.effects import EffectType, effects


class EffectLabel(Static):

    text: reactive[str] = reactive("")
    height: var[int] = var(0)
    width: var[int] = var(0)
    effect: var[EffectType] = var("Beams")
    config: var[dict[str, Any]] = var({})

    class EffectFinished(Message):

        def __init__(self, effect: EffectType) -> None:
            self.effect = effect
            super().__init__()

    def __init__(
        self, text: str, effect: EffectType = "Beams", config: dict[str, Any] = {}
    ) -> None:
        super().__init__(text)

        self.text = text
        self.effect = effect
        self.config = config
        self.width = max(len(line) for line in text.split("\n"))
        self.height = text.count("\n")
        self.styles.width = self.width + 2
        self.styles.height = self.height + 2

    async def on_mount(self) -> None:
        self.run_worker(self.run_effect(), exclusive=True)

    async def run_effect(self):
        effect: BaseEffect = effects[self.effect](self.text)
        for key in self.config:
            if hasattr(effect.effect_config, key):
                setattr(effect.effect_config, key, self.config[key])

        effect.terminal_config.canvas_width = self.width
        effect.terminal_config.canvas_height = self.height
        frames = []
        for frame in effect:
            frames.append(frame)

        for frame in frames:
            self.text = frame
            self.update(Text.from_ansi(self.text))
            await asyncio.sleep(0)
        self.post_message(self.EffectFinished(self.effect))


class SplashScreen(ModalScreen):
    text: reactive[str] = reactive("")
    effect: var[EffectType] = var("Beams")
    config: var[dict[str, Any]] = var({})

    CSS = """
    EffectLabel {
        background: $background;
    }
    Container {
        align: center middle;
    }
    """

    BINDINGS = [
        ("escape", "cancel", "Cancel"),
    ]

    def __init__(
        self, text: str, effect: EffectType = "Beams", config: dict[str, Any] = {}
    ) -> None:
        super().__init__()
        self.text = text
        self.effect = effect
        self.config = config

    def action_cancel(self) -> None:
        self.dismiss()

    @on(EffectLabel.EffectFinished)
    def on_effect_finished(self, message: EffectLabel.EffectFinished) -> None:
        self.dismiss(message)

    def compose(self) -> ComposeResult:
        with Container():
            yield EffectLabel(
                text=self.text,
                effect=self.effect,
                config=self.config,
            )
