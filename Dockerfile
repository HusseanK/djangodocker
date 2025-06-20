FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.7.12 /uv /uvx /bin/

ADD . /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1 

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]