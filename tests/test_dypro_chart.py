from unittest import TestCase

from parameterized import parameterized

from src.dypro.modules.normal import (
    NormalMeanVarChart,
    NormalMeanSChart,
    NormalMeanRChart,
)


class TestDypro(TestCase):
    def setUp(self) -> None:
        self.sample_size = 10
        self.alpha = 0.0027

    @parameterized.expand(
        [
            (0, 1.7511),
            (0.1, 1.7481),
            (0.2, 1.7392),
            (0.3, 1.7239),
            (0.4, 1.7014),
            (0.5, 1.6702),
            (0.6, 1.6281),
            (0.7, 1.5704),
            (0.8, 1.4862),
            (0.9, 1.3325),
        ]
    )
    def test_dypro_normal_mean_var_chart(self, k1, k2):
        chart = NormalMeanVarChart(self.alpha)
        power = round(chart.power(k1, k2, self.sample_size), 4)
        self.assertEqual(power, 0.5)

    @parameterized.expand(
        [
            (0, 1.73405),
            (0.1, 1.73116),
            (0.2, 1.72237),
            (0.3, 1.70724),
            (0.4, 1.68497),
            (0.5, 1.6542),
            (0.6, 1.61253),
            (0.7, 1.55535),
            (0.8, 1.47189),
            (0.9, 1.31961),
        ]
    )
    def test_dypro_normal_mean_s_chart(self, k1, k2):
        chart = NormalMeanSChart(self.alpha)
        power = round(chart.power(k1, k2, self.sample_size), 4)
        self.assertEqual(power, 0.5)

    @parameterized.expand(
        [
            (0, 1.8669),
            (0.1, 1.8635),
            (0.2, 1.8531),
            (0.3, 1.8354),
            (0.4, 1.8094),
            (0.5, 1.7735),
            (0.6, 1.7252),
            (0.7, 1.659),
            (0.8, 1.5626),
            (0.9, 1.3861),
        ]
    )
    def test_dypro_normal_mean_r_chart(self, k1, k2):
        chart = NormalMeanRChart(self.alpha)
        power = round(chart.power(k1, k2, self.sample_size), 4)
        self.assertEqual(power, 0.5)
