FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y cron git python3-pip \
    build-essential libpoppler-cpp-dev \
    pkg-config python3-dev python3-pil tesseract-ocr && \
    pip3 install pdftotext requests beautifulsoup4 pyexcel-ods3 pytesseract pymongo

COPY cron_crawler /etc/cron.d/cron_crawler

COPY store_electric_factor.py /root/store_electric_factor.py

RUN chmod 0644 /etc/cron.d/cron_crawler && \
    touch /var/log/cron.log && \
    crontab /etc/cron.d/cron_crawler && \
    git clone https://github.com/peter279k/gwp-factors
