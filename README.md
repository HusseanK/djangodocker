# Django + Postgres Docker Demo

This project demonstrates how to run a Django app with PostgreSQL using Docker.

This was a test-project before my actual project (React/Django/Postgres + Docker)


Development server exposed on  port 8000
DB exposed on port 5432


# Prerequisites
Docker

# Running the app:
docker-compose up --build

# Stopping + cleanup
docker-compose down

## API

Simple notes API using Django REST Framework (DRF).
Includes basic CRUD functionality for notes: 'title', 'content'

with tests using Djangos 'TestCase' and DRF's 'APIClient'

### Example (POST)

POST /api/notes/
```json
{
    "title":"Test",
    "content":"This is a test note"
}