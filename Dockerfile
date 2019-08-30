FROM node:10 as client
WORKDIR /app/rh/client
COPY ./rh/client/package.json ./rh/client/yarn.lock ./
RUN NOYARNBUILD=1 yarn install
COPY ./rh/client/ ./
RUN yarn build


FROM python:3.6-buster as build
RUN pip install -U pip pipenv
WORKDIR /app
ENV PIPENV_VENV_IN_PROJECT=1 DJANGO_SETTINGS_MODULE=rh.settings.deploy SECRET_KEY=s ALLOWED_HOSTS=*
COPY Pipfile Pipfile.lock setup.py setup.cfg ./
COPY rh/__init__.py ./rh/__init__.py
RUN pipenv install --deploy
COPY . .
COPY --from=client /app/rh/client ./rh/client
RUN pipenv run manage.py collectstatic --noinput


FROM python:3.6-slim-buster
WORKDIR /app
ENV PATH=/app/.venv/bin:${PATH} DJANGO_SETTINGS_MODULE=rh.settings.deploy PORT=8000
RUN set -ex && \
    apt-get update -qq && apt-get install --no-install-recommends -y libpq5 && rm -rf /var/lib/apt/lists/* && \
    groupadd -r rh && useradd --uid=1000 --no-log-init -r -g rh rh && \
    mkdir -p /app && chown rh:rh /app
COPY --from=build /etc/mime.types /etc/mime.types
COPY --from=build --chown=rh:rh /app ./
# stats
EXPOSE 1717/tcp
# web server
EXPOSE 8000/tcp
USER rh
CMD uwsgi --ini=uwsgi.ini

