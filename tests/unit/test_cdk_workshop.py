from aws_cdk import Stack, aws_lambda as _lambda, assertions
from cdk_workshop.hitcounter import HitCounter


def test_dynamodb_table_created():
    stack = Stack()
    HitCounter(
        stack,
        "HitCounter",
        downstream=_lambda.Function(
            stack,
            "TestFunction",
            runtime=_lambda.Runtime.NODEJS_14_X,
            handler="hello.handler",
            code=_lambda.Code.from_asset("lambda"),
        ),
    )
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::DynamoDB::Table", 1)
