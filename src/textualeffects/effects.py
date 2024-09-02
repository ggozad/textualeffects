import importlib
import pkgutil
from typing import Literal

import terminaltexteffects.effects

EffectType = Literal[
    "Beams",
    "BinaryPath",
    "Blackhole",
    "BouncyBalls",
    "Bubbles",
    "Burn",
    "ColorShift",
    "Crumble",
    "Decrypt",
    "ErrorCorrect",
    "Expand",
    "Fireworks",
    "Matrix",
    "MiddleOut",
    "OrbittingVolley",
    "Overflow",
    "Pour",
    "Print",
    "Rain",
    "RandomSequence",
    "Rings",
    "Scattered",
    "Slice",
    "Slide",
    "Spotlights",
    "Spray",
    "Swarm",
    "SynthGrid",
    "Unstable",
    "VHSTape",
    "Waves",
    "Wipe",
]

effects = {}
effect_args = {}
for module_info in pkgutil.iter_modules(
    terminaltexteffects.effects.__path__, terminaltexteffects.effects.__name__ + "."
):
    module = importlib.import_module(module_info.name)
    if hasattr(module, "get_effect_and_args"):
        effect_class, arg_class = module.get_effect_and_args()
        effects[effect_class.__name__] = effect_class
        effect_args[effect_class.__name__] = arg_class
