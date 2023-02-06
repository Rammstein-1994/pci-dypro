from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
)
from constructs import Construct


class DyproLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)
        self.create_lambda(id_)

    def create_lambda(self, stack_name: str) -> _lambda.Function:
        return _lambda.DockerImageFunction(
            self,
            f"{stack_name}-Lamda".replace("-", ""),
            function_name=f"{stack_name}-lambda".lower(),
            timeout=Duration.seconds(300),
            code=_lambda.DockerImageCode.from_image_asset("."),
            architecture=_lambda.Architecture.ARM_64,
        )
