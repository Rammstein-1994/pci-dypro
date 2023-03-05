from typing import Any

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser

from src.handler.event_handler import DyproHandler

logger = Logger()


class Parameters:
    k1: float
    k2: float
    sample_size: int


@event_parser(model=Parameters)
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    event_hanlder = DyproHandler(event)
    return event_hanlder.handle()
