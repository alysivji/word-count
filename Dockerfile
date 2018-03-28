FROM python:3.6.4-slim-jessie

LABEL maintainer="Aly Sivji <alysivji@gmail.com>" \
      description="Development image for Word Count Webapp"

WORKDIR /home/web/

COPY requirements.txt requirements_dev.txt /tmp/
COPY . /home/web

RUN groupadd -g 901 -r sivdev && \
    useradd -g sivdev -r -u 901 sivdev_user && \
    pip install --no-cache-dir -r /tmp/requirements_dev.txt

EXPOSE 5000

# Switch from root user for security
USER sivdev_user

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
