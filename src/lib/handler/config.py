from enum import Enum

from lib.dypro.modules.normal import (
    NormalMeanVarChart,
    NormalMeanSChart,
    NormalMeanRChart,
)


class ChartType(Enum):
    NormalMeanVar = NormalMeanVarChart
    NormalMeanS = NormalMeanSChart
    NormalMeanR = NormalMeanRChart
