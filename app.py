#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_stack.stack import TemplateStack


app = cdk.App()
TemplateStack(app, "InfraTemplateStack")

app.synth()
