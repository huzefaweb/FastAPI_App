# Full-Stack FastAPI & React Application

This repository contains two services:

1. **backend/**: A FastAPI application with MongoDB, containerized via Docker Compose
2. **frontend/**: A React (Vite) application handling user signup, login, and signout flows

---

## 📂 Repository Structure

```
├── backend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── app/
│   ├── tests/
│   ├── .env.example
│   └── backend_readme.md       # Documentation for backend service

├── frontend/
│   ├── src/
│   ├── public/
│   ├── .env.example
│   ├── package.json
│   └── frontend_readme.md      # Documentation for frontend service

└── README.md                   # ← You are here
```

---

## 🚀 Getting Started

Follow these steps to spin up both services locally and test end-to-end functionality.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Review environment variables

- **backend/**: Copy `backend/.env.example` to `backend/.env` and fill in the values (e.g., `MONGODB_URI`, `JWT_SECRET`, etc.).
- **frontend/**: Copy `frontend/.env.example` to `frontend/.env` and configure the API base URL (e.g., `VITE_API_BASE_URL=http://localhost:8000`).

### 3. Run the App

From the root of this repo:

```bash
docker-compose up --build
```

- Backend API will be available at `http://localhost:8000`
- MongoDB is running in a Docker container on the default port (27017)
- backend pytests will also run with docker if you don't want it comment it out in the docker_compose.yml
- Frontend app will be available at `http://localhost:3000` (or another port as displayed).

### 6. Test the End-to-End Flow

1. Open your browser to `http://localhost:3000`.
2. Use the **Sign Up** page to register a new user.
3. Log in with that user on the **Log In** page.
4. Once authenticated, navigate to the **Home** page and verify the **Sign Out** button logs you out.

---

## 📄 Service Documentation

- For detailed configuration, endpoint specs, and additional commands, see:
  - [backend/backend\_readme.md](backend/backend_readme.md)
  - [frontend/frontend\_readme.md](frontend/frontend_readme.md)

---

## 🧹 Cleanup & Tips

- Make sure to add `node_modules/` and `.venv/` to your `.gitignore`.
- Remove any stale build artifacts before committing.

---

## 🎉 You're All Set!

Congratulations on setting up your full-stack FastAPI & React application. Feel free to customize further or deploy to your preferred cloud platform!

