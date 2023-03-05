from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser, parse

from src.handler.event_handler import DyproHandler


class Parameters:
    k1: float
    k2: float
    sample_size: int


@event_parser(model=Parameters)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    event_hanlder = DyproHandler(event)
    return event_hanlder.handle()
