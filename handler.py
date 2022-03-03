import json


def hello(event, context):
   body = {
       "message": "Go Serverless v1.0!",
       "input": event
   }

   response = {
       "statusCode": 200,
       "body": json.dumps(body)
   }
   return response


def calculator(event, context):
    print(event)
    body = json.loads(event["body"])
    number1 = body["number1"]
    number2 = body["number2"]
    sum = number1 + number2
    return {
        'statusCode': 200,
        "body": json.dumps(str(number1) + ' + ' + str(number2) + ' = ' + str(sum))
    }

#event = {'resource': '/calculator', 'path': '/calculator', 'httpMethod': 'POST', 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'NO', 'Content-Type': 'text/plain', 'Host': 'pn634097dh.execute-api.eu-west-1.amazonaws.com', 'Postman-Token': '91b8b2e5-3814-4664-9f3c-04f3d33968b6', 'User-Agent': 'PostmanRuntime/7.29.0', 'Via': '1.1 f46773a8236e136c4f6648dd79a7af8e.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'HS9m3vHHLDXeMvaMRDjbEhAMfeJ-6Er2lhJmP0GqRKVskK4v1h9Q2A==', 'X-Amzn-Trace-Id': 'Root=1-6220badc-2ec672155c684f596e38379f', 'x-api-key': 'lRYczHFLnK54I3qGFYRwR9xWCPBdaymB8syvjBz6', 'X-Forwarded-For': '158.39.193.221, 130.176.182.47', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['NO'], 'Content-Type': ['text/plain'], 'Host': ['pn634097dh.execute-api.eu-west-1.amazonaws.com'], 'Postman-Token': ['91b8b2e5-3814-4664-9f3c-04f3d33968b6'], 'User-Agent': ['PostmanRuntime/7.29.0'], 'Via': ['1.1 f46773a8236e136c4f6648dd79a7af8e.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['HS9m3vHHLDXeMvaMRDjbEhAMfeJ-6Er2lhJmP0GqRKVskK4v1h9Q2A=='], 'X-Amzn-Trace-Id': ['Root=1-6220badc-2ec672155c684f596e38379f'], 'x-api-key': ['lRYczHFLnK54I3qGFYRwR9xWCPBdaymB8syvjBz6'], 'X-Forwarded-For': ['158.39.193.221, 130.176.182.47'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'he7pu5', 'resourcePath': '/calculator', 'httpMethod': 'POST', 'extendedRequestId': 'OaIiiHJzjoEF6jg=', 'requestTime': '03/Mar/2022:12:55:56 +0000', 'path': '/api/calculator', 'accountId': '074818079789', 'protocol': 'HTTP/1.1', 'stage': 'api', 'domainPrefix': 'pn634097dh', 'requestTimeEpoch': 1646312156811, 'requestId': '66fdc49b-7ebd-4b8e-b784-7e89f443d8eb', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'lRYczHFLnK54I3qGFYRwR9xWCPBdaymB8syvjBz6', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': None, 'apiKeyId': 'sahh65qo52', 'userAgent': 'PostmanRuntime/7.29.0', 'accountId': None, 'caller': None, 'sourceIp': '158.39.193.221', 'accessKey': None, 'cognitoAuthenticationProvider': None, 'user': None}, 'domainName': 'pn634097dh.execute-api.eu-west-1.amazonaws.com', 'apiId': 'pn634097dh'}, 'body': '{\r\n    "number1": 1,\r\n    "number2": 2\r\n}\r\n', 'isBase64Encoded': False}
#calculator(event,None)

