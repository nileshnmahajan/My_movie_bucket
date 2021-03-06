FROM python:3.6.8
ENV  PYTHONUNBUFFERED 1
RUN makedir /app
WORKDIR /app

ADD . /app
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT 8888

#install system dependencies

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        mysql-client\
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev


COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/

