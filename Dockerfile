FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.11

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY api api

CMD ["api.main.handler"]
