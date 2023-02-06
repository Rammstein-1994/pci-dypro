FROM public.ecr.aws/lambda/python:3.9-arm64

LABEL maintainer="happydog"

COPY src/lambda_function.py ./
COPY src ./src
# Copies requirements.txt file into the container
COPY requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt --target ./

# Points to the handler function of your lambda function
CMD [ "lambda_function.lambda_handler" ]
