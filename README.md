# Mood Architect

A therapeutic affirmation generator built with Vue.js and Django.

## How to Run Locally

### Backend Setup

1. Navigate to the backend directory:
```bash
   cd backend
```

2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the `backend/` directory with:
```
   OPENAI_API_KEY=your-openai-api-key-here
   SECRET_KEY=your-django-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:5173
```

5. Start the Django server:
```bash
   python manage.py runserver
```

Backend will run at: `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
   cd frontend
```

2. Install dependencies:
```bash
   npm install
```

3. Start the development server:
```bash
   npm run dev
```

Frontend will run at: `http://localhost:5173`

## Environment Variables

Create a `.env` file in the `backend/` directory:

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | `sk-proj-...` |
| `SECRET_KEY` | Django secret key | Any random string |
| `DEBUG` | Debug mode (use `False` in production) | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | Frontend URL for CORS | `http://localhost:5173` |

## Deployment

### Backend (Render/Railway)
TBD

### Frontend (Vercel)
TBD

## Live URLs

- **Frontend:** TBD
- **Backend:** TBD
