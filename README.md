# python-serverless-example

#### Install and setup virtualenv

`sudo pip install virtualenv`

`virtualenv venv --python=python3` make sure am in python-serverless-example folder

`source venv/bin/activate`

`pip3 install -r requirements.txt`

#### Make sure using serverless v1.20.2

A bug introduced in serverless 1.21 introduces a bug that messes up the python dependency. Let's stick with 1.20 until it's fixed.

`npm install serverless@1.20.2 -g`

#### Install serverless-python-requirements plugin

`npm install --save serverless-python-requirements`

### Test locally

`sls invoke local --function example `

### Deploy to dev

`sls deploy --stage=dev`

### Invoke Lambda

Same idea as testing locally. 

`sls invoke --stage=dev --function example -p data.json --log`

### Documentation
https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
https://serverless.com/framework/docs/providers/aws/
https://aws.amazon.com/sdk-for-python/
