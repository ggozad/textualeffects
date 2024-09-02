import asyncio
from typing import Any

from rich.text import Text
from terminaltexteffects.engine.base_effect import BaseEffect
from textual.reactive import reactive, var
from textual.widgets import Static

from textualeffects.effects import EffectType, effects


class EffectLabel(Static):

    text: reactive[str] = reactive("")
    height: var[int] = var(0)
    width: var[int] = var(0)
    effect: var[str] = var("beams")
    config: var[dict[str, Any]] = var({})

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
