# Auth App v1 — Backend

## Overview

This is the FastAPI backend for **Auth App v1**, providing signup, login, JWT-based access & refresh tokens, sign-out (revoking refresh tokens), and a protected sample route.\
It uses MongoDB (Motor), Docker & Docker Compose for containerization, and pytest for tests.

---

## Prerequisites

- Python 3.10+
- MongoDB (local or Docker)
- Docker & Docker Compose (for containerized setup)

---

## Environment

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and fill in:
   ```dotenv
   MONGODB_URI=mongodb://mongo:port_number
   DB_NAME=database_name

   SECRET_KEY=your_secret_key_here
   ALGORITHM=Algo_key
   ACCESS_TOKEN_EXPIRE_MINUTES=Numbers
   REFRESH_TOKEN_EXPIRE_MINUTES=Numbers   # 7 days
   ```

---

## Local Setup

1. **Create & activate** a virtual environment

   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```

2. **Install** dependencies

   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

3. **Start MongoDB** (if not using Docker)

   ```bash
   mongod --dbpath <your-db-path>
   ```

4. **Run** the server

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Browse** the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Docker Compose

From the project root (`auth_app_v1/`), bring up the backend service and MongoDB:

```bash
docker-compose up --build
```

- **Backend**: [http://localhost:8000](http://localhost:8000)
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **MongoDB**: container port 27017 (host port configurable)

To tear down:

```bash
docker-compose down
```

---

## Tests

Run unit tests with pytest:

```bash
cd backend
pytest -q
```

All tests should pass green.

---

## API Endpoints

### Authentication (`/auth`)

- **POST** `/auth/signup`\
  Creates a new user.\
  **Request Body**:

  ```json
  {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice@example.com",
    "phone": "+1234567890",
    "address": "123 Main St",
    "password": "secret123"
  }
  ```

  **Response** (`201 Created`):

  ```json
  {
    "access_token": "<jwt>",
    "refresh_token": "<jwt>"
  }
  ```

- **POST** `/auth/login`\
  Authenticates a user.\
  **Request Body**:

  ```json
  {
    "email": "alice@example.com",
    "password": "secret123"
  }
  ```

  **Response** (`200 OK`):

  ```json
  {
    "access_token": "<jwt>",
    "refresh_token": "<jwt>"
  }
  ```

- **POST** `/auth/signout`\
  Revokes the user’s refresh token.\
  **Headers**:

  ```
  Authorization: Bearer <access_token>
  ```

  **Response**: `204 No Content`

### Protected

- **GET** `/protected`\
  A sample protected route—requires a valid access token.\
  **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
  **Response** (`200 OK`):
  ```json
  {
    "message": "Hello, user <user_id>"
  }
  ```

---

## License

MIT © Huzefa Ahmed

