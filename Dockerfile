# ベースイメージ作成
FROM python:3.7

# requirements.txtをコピー
COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
# pipアップグレード
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD

# 作業ディレクトリ指定
WORKDIR /workdir

EXPOSE 8080