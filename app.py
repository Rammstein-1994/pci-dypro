#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_stack.stack import DyproLambdaStack


app = cdk.App()
stack_name = os.environ.get("STACK_NAME", "PCI-Dypro")
DyproLambdaStack(app, stack_name)

app.synth()
