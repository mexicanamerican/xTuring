from typing import Optional

from xturing.engines.distilgpt2_engine import DistilGPT2Engine, DistilGPT2LoraEngine

from .causal import CausalLoraModel, CausalModel


class DistilGPT2(CausalModel):
    config_name: str = "distilgpt2"

    def __init__(self, weights_path: Optional[str] = None):
        super().__init__(DistilGPT2Engine.config_name, weights_path)


class DistilGPT2LORA(CausalLoraModel):
    config_name: str = "distilgpt2_lora"

    def __init__(self, weights_path: Optional[str] = None):
        super().__init__(DistilGPT2LoraEngine.config_name, weights_path)
