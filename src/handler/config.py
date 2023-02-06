from enum import Enum

from ..dypro.modules.normal import (
    NormalMeanVarChart,
    NormalMeanSChart,
    NormalMeanRChart,
)


class ChartType(Enum):
    NormalMeanVar = NormalMeanVarChart
    NormalMeanS = NormalMeanSChart
    NormalMeanR = NormalMeanRChart
