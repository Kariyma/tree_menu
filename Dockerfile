FROM python:3.10-slim AS tree_menu-builder

WORKDIR /opt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY ./src/requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends python-dev && \
     pip install --upgrade pip \
     && pip install wheel && pip3 wheel -r requirements.txt --wheel-dir=/opt/wheels


FROM python:3.10-slim

COPY --from=tree_menu-builder /opt /opt

WORKDIR /opt/content

COPY ./src .
COPY .env /opt


RUN mkdir -p /opt/content/staticfiles && mkdir -p /opt/content/mediafiles && \
    pip install --no-index --find-links=/opt/wheels -r requirements.txt

RUN chmod +x  ./start.sh

ENTRYPOINT ["./start.sh"]