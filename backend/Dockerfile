# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}

FROM python:${INSTALL_PYTHON_VERSION}-slim AS builder
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    python3-dev
RUN pip install poetry
RUN poetry config installer.max-workers 10

COPY pyproject.toml .
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

# ================================= DEVELOPMENT ================================
FROM builder AS development

CMD [ "fastapi", "dev"]


# ================================= PRODUCTION =================================
FROM builder AS production

COPY . .

RUN chmod +x ./scripts/pre-init.sh
ENTRYPOINT [ "./scripts/pre-init.sh" ]

CMD [ "fastapi", "run" ]
