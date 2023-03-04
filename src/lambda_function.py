from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext

from src.handler.event_handler import DyproHandler


def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    event_hanlder = DyproHandler(event)
    return event_hanlder.handle()
