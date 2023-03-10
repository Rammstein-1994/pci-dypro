from typing import Any

from aws_xray_sdk.core import xray_recorder

from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.handler.event_handler import DyproHandler

logger = Logger()
metrics = Metrics()
tracer = Tracer()


@xray_recorder.capture("lambda_handler")
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    return DyproHandler(event).handle()
