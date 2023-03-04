from enum import Enum

from ..dypro.modules.normal import (
    NormalMeanVarChart,
    NormalMeanSChart,
    NormalMeanRChart,
)


class Parameter:
    k1: float
    k2: float
    sample_size: int


class ChartType(Enum):
    NormalMeanVar = NormalMeanVarChart
    NormalMeanS = NormalMeanSChart
    NormalMeanR = NormalMeanRChart
