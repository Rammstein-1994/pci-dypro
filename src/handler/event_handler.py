from typing import Protocol, Dict, Any

from aws_xray_sdk.core import xray_recorder

from ..dypro.modules.normal import NormalMeanVarChart


class BaseHandler(Protocol):
    """Base class for all event handlers."""

    def __init__(self, event):
        ...

    def handle(self):
        ...


class DyproHandler:
    """Handler for Dypro Lambda."""

    def __init__(self, event: Dict[str, Any]) -> None:
        self.chart = NormalMeanVarChart()
        self.sample_size = event["sample_size"]
        self.k1 = event["k1"]
        self.k2 = event["k2"]

    @xray_recorder.capture("DyproHandler.handle")
    def handle(self) -> dict[str, Any]:
        self.power = round(self.chart.power(self.k1, self.k2, self.sample_size), 4)
        return {
            "statusCode": 200,
            "body": f"Lambda was: invoked successfully. Power = {self.power}",
        }
