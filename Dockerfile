FROM python:3.12
RUN apt-get update \
    && apt-get -y install tesseract-ocr
WORKDIR /bot
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py ./
CMD [ "python", "./bot.py"]