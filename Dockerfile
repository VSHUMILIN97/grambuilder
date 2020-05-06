FROM python:3.6.9-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100
ENV POETRY_VERSION 0.12.11
WORKDIR /opt/grambuilder
COPY . ./
RUN pip install poetry==$POETRY_VERSION
RUN  poetry config settings.virtualenvs.create false \
&& poetry install --no-dev --no-ansi --no-interaction
CMD ["gunicorn", "web.servlet:app", "-c", "guniconf.py"]
