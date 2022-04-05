# from constructs import Construct
# from aws_cdk import (
#     aws_lambda as _lambda,
# )

# class cdkStack(Stack):
#     def __init__(self, scope: Construct, id: str, **kwargs) -> None:
#         super().__init__(scope, id, **kwargs)

#         my_lambda = _lambda.Function(
#             self, 'lambda_handler',
#             runtime = _lambda.Runtime.PYTHON_3_7,
#             code = _lambda.Code.from_asset('lambda'),
#             handler = 'lambda_function.lambda_handler'
#         )


from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda
)
from awsFolder import lambda_function


class CdkStackShop(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HellowHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='lambda_function.lambda_handler'
        )