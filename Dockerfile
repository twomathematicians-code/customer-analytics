FROM python:3.11-slim
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install poetry==1.8.3
WORKDIR /app
COPY pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-root
COPY src/ src/ configs/ configs/
RUN useradd -m -r custuser && chown -R custuser /app
USER custuser
EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
