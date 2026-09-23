variable "region" {
  description = "The AWS region to deploy the resources"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = "normative-query-lambda"
}

variable "api_gateway_name" {
  description = "The name of the API Gateway"
  type        = string
  default     = "normative-query-api"
}

variable "stage_name" {
  description = "The stage name for the API Gateway"
  type        = string
  default     = "prod"
}

variable "lambda_memory_size" {
  description = "The amount of memory allocated to the Lambda function in MB"
  type        = number
  default     = 128
}

variable "lambda_timeout" {
  description = "The maximum execution time of the Lambda function in seconds"
  type        = number
  default     = 30
}

variable "lambda_role" {
  description = "The ARN of the IAM role that the Lambda function assumes"
  type        = string
}

variable "lambda_handler" {
  description = "The handler for the Lambda function"
  type        = string
  default     = "app.main.lambda_handler"
}