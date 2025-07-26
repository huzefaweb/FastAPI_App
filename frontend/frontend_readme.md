# Frontend Service Documentation

This document covers the **React (Vite)** frontend deliverables, including:

- UI Implementation
- Integration with Backend Endpoints
- JWT Storage & Refresh
- Route Protection
- Design & Deployment

---

## 🔨 UI Implementation

**Pages & Components:**

1. **Signup** (`/signup`)

   - Form fields: First Name, Last Name, Email, Phone, Address, Password
   - Validation: required fields, password strength
   - On submit: POST to `/auth/signup`, store `access_Token`, redirect to Home

2. **Login** (`/login`)

   - Form fields: Email, Password
   - Validation: required
   - On submit: POST to `/auth/login`, store `access_Token` & `refresh_Token`, redirect to Home

3. **Home** (`/`)

   - Welcome message + user info
   - **Sign Out** button: triggers POST to `/auth/signout`, clears tokens, redirect to Login

4. **ProtectedRoute** component

   - Wraps routes, checks for valid `access_Token` in `localStorage`
   - Redirects to `/login` if missing or expired (see example in App router)

---

## 🔗 Integration with Backend

- **API Base URL** configured via `VITE_API_BASE_URL` in `.env`
- **HTTP Client**: using `fetch` or `axios`
  ```js
  const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE_URL })
  api.interceptors.request.use(config => {
    const token = localStorage.getItem('access-Token')
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
  })
  ```
- **Signup Flow**:
  ```js
  await api.post('/auth/signup', {...formValues})
    .then(res => localStorage.setItem('access_Token', res.data.access_token))
  ```
- **Login Flow**:
  ```js
  await api.post('/auth/login', { email, password })
    .then(res => {
      localStorage.setItem('access_Token', res.data.access_token)
      localStorage.setItem('refresh_Token', res.data.refresh_token)
    })
  ```
- **Sign Out**:
  ```js
  await api.post('/auth/signout')
  localStorage.removeItem('access_Token')
  localStorage.removeItem('refresh_Token')
  ```

---

## 🛡 JWT Storage & Refresh

- **Storage**: `localStorage` keys `access_Token`, `refresh_Token`
- **Auto-Refresh**:
  - Intercept 401 responses, call `/auth/refresh` with `refresh_Token`
  - On success: update `access_Token`, retry original request
  - On failure: redirect to `/login`

```js
api.interceptors.response.use(
  res => res,
  async err => {
    if (err.response?.status === 401) {
      const refresh = localStorage.getItem('refresh_Token')
      if (!refresh) return Promise.reject(err)

      const { data } = await api.post('/auth/refresh', { token: refresh })
      localStorage.setItem('access_Token', data.access_token)
      err.config.headers.Authorization = `Bearer ${data.access_token}`
      return api(err.config)
    }
    return Promise.reject(err)
  }
)
```

---

## 🚧 Route Protection

Wrap protected routes in `<ProtectedRoute>` as shown in `App.jsx`:

```jsx
<Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
<Route path="/signout" element={<ProtectedRoute><SignOut /></ProtectedRoute>} />
```

Ensure unauthenticated users are always redirected to `/login`.

---

## 🎨 Design & Deployment

- **Design Freedom**: Feel free to use AI design tools (e.g., Lovable, Figma-to-React) to craft polished UI.
- **Styling**: Tailwind CSS or your preferred CSS-in-JS approach.

**Optional Deployment**:

1. **Vercel**:

   - Connect GitHub repo to Vercel
   - Set `VITE_API_BASE_URL` in Vercel environment settings
   - Deploy the `frontend/` directory

2. **Netlify**:

   - Similar setup; ensure build command `npm run build`, publish `dist/`

---

## 📄 Running Locally

1. Copy `.env.example` to `.env`, set `VITE_API_BASE_URL=http://localhost:8000`
2. Install dependencies and start dev server:
   ```bash
   npm install
   npm run dev
   ```
3. Open `http://localhost:3000`

---

## 🎉 You're Ready!

Your React frontend is now configured for secure auth flows, full integration with the FastAPI backend, and easy deployment.

