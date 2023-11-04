# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}

FROM python:${INSTALL_PYTHON_VERSION}-slim AS builder
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

EXPOSE 8000

RUN pip install poetry
RUN poetry config installer.max-workers 10

COPY pyproject.toml .
RUN poetry install --no-interaction --no-ansi


# ================================= DEVELOPMENT ================================
FROM builder AS development

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "api.main:app", "--reload" ]


# ================================= PRODUCTION =================================
FROM builder AS production

COPY . .

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "api.main:app" ]
