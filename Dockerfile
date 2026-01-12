FROM python:3.12-slim
LABEL maintainer="agent1237@datawhalechina.cn"
LABEL team="agent①②③⑦"
LABEL project="hello-agents"
LABEL git.repo="https://github.com/pamdla/hello-agents"

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /learning

COPY requirements.txt .

RUN apt update \
    && apt install -y --no-install-recommends \
    && apt install -y git wget make gcc g++ \
    && apt autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install --no-cache-dir -r requirements.txt
