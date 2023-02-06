from typing import Protocol, Dict, Any

from lib.dypro.modules.normal import NormalMeanVarChart
from lib.utils import Decimals


class BaseEventHandler(Protocol):
    """Base class for all event handlers."""

    def __init__(self, event):
        ...

    def handle(self):
        ...


class DyproEventHandler(BaseEventHandler):
    """Handler for Dypro Lambda."""

    def __init__(self, event: Dict[str, Any]) -> None:
        self.chart = NormalMeanVarChart()
        self.sample_size = event["sample_size"]
        self.k1 = event["k1"]
        self.k2 = event["k2"]

    @Decimals(decimals=4)
    def handle(self) -> float:
        return self.chart.power(self.k1, self.k2, self.sample_size)
