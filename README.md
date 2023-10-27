# fastapi-lambda
Run FastAPI locally in a Docker container and then deploy it to AWS Lambda.

## Installation

First, install

* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

and then run

```bash
yarn install
```

## Local development

To launch the development server, ensure Docker is running and then run

```bash
yarn dev
```

The development server will be running in a container that can be accessed at
[http://localhost:8000/](http://localhost:8000/).

## Deployment

To deploy AWS, ensure Docker is running and then run

```bash
cdk deploy --profile $AWS_PROFILE
```

If deployment is successful, the AWS CDK will print the API endpoint to the
console. 

To tear down the AWS deployment, run

```bash
cdk destroy --profile $AWS_PROFILE
```

`$AWS_PROFILE` is set using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
