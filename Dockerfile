FROM python:3.10 as base
FROM base as production 
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install
COPY .env.template /app/
COPY todo_app /app/todo_app
RUN cp .env.template .env
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
FROM base as development
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install
COPY .env.template /app/
COPY todo_app /app/todo_app
RUN cp .env.template .env
ENTRYPOINT poetry run flask run --host=0.0.0.0
