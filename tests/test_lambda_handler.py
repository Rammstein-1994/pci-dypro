from unittest import TestCase

from src.lambda_function import lambda_handler


class TestLambdaHandler(TestCase):
    def test_lambda_handler_with_expected(self):
        event = {"k1": 0.2, "k2": 1.7392, "sample_size": 10}
        response = lambda_handler(event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(
            response["body"], "Lambda was: invoked successfully. Power = 0.5"
        )
