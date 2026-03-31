FROM python:3.12.3-alpine as base
WORKDIR /mates_backend


FROM base as dev
COPY requirements/requirements.dev.txt .
RUN pip install -r requirements.dev.txt
COPY . .
RUN chmod +x build.sh
CMD [ "./build.sh" ]


FROM base as prod
COPY requirements/requirements.prod.txt .
RUN pip install -r requirements.prod.txt
COPY build.sh .
RUN chmod +x build.sh
COPY . .
CMD [ "sh","./build.sh" ]