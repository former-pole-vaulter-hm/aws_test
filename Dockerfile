# ベースイメージ作成
FROM python:3.7

# requirements.txtをコピー
COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
# pipアップグレード
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 作業ディレクトリ指定
WORKDIR /workdir

EXPOSE 8080