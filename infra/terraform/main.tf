provider "aws" {
  region = var.region
}

resource "aws_lambda_function" "normative_query" {
  function_name = var.lambda_function_name
  role         = var.lambda_role
  handler      = var.lambda_handler
  runtime      = "python3.13"
  memory_size  = var.lambda_memory_size
  timeout      = var.lambda_timeout
  
  environment {
    variables = {
      REGION = var.region
    }
  }
  
  source_code_hash = filebase64sha256("./app/main.py")
  filename         = "app/main.py"
  
  depends_on = [
    module.iam_role
  ]
}

resource "aws_api_gateway_rest_api" "normative_query" {
  name        = var.api_gateway_name
  description = "API Gateway for normative queries"
}

resource "aws_api_gateway_resource" "query" {
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  parent_id  = aws_api_gateway_rest_api.normative_query.root_resource_id
  path_part  = "query"
}

resource "aws_api_gateway_method" "post" {
  rest_api_id   = aws_api_gateway_rest_api.normative_query.id
  resource_id   = aws_api_gateway_resource.query.id
  http_method   = "POST"
  authorization = "NONE"
  
  request_parameters = {
    "method.request.header.Content-Type" = true
  }
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  resource_id = aws_api_gateway_resource.query.id
  http_method = aws_api_gateway_method.post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.normative_query.invoke_arn
  
  request_templates = {
    "application/json" = "$input.json('$')"
  }
}

resource "aws_api_gateway_deployment" "normative_query" {
  depends_on = [
    aws_api_gateway_integration.lambda
  ]
  
  rest_api_id = aws_api_gateway_rest_api.normative_query.id
  stage_name  = var.stage_name
}

output "api_gateway_url" {
  value = aws_api_gateway_deployment.normative_query.invoke_url
}