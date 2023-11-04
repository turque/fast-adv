# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=3.11

FROM python:3.11-slim AS builder
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app


RUN pip install poetry
RUN poetry config installer.max-workers 10

COPY pyproject.toml .
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

# ================================= DEVELOPMENT ================================
FROM builder AS development

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "api.main:app", "--reload" ]


# ================================= PRODUCTION =================================
FROM builder AS production

COPY . .

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "api.main:app" ]
