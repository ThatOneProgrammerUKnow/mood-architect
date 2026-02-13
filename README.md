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

## Deployment

### Backend (Render)
1. Create a new Web Service on Render.
2. Connect your GitHub repository and select the backend folder.
3. Set the Build Command:
```bash
pip install -r requirements.txt
```
4. Set the Start Command:
```bash
gunicorn backend.wsgi
```
5. Add the following Environment Variables on Render:
  - OPENAI_API_KEY
  - SECRET_KEY
  - DEBUG=False
6. Deploy the project
### Frontend (Vercel)
1. Import the repository into Vercel.
2. Set the root directory to the frontend folder.
3. In the Vercel dashboard Environment Variables, add:
- VITE_API_URL=https://your-render-backend-url
4. Deploy the project.
5. Vercel will provide a live frontend URL.

## Live URLs
- **Frontend:** https://mood-architect-two.vercel.app/
- **Backend:** https://mood-architect-backend-ov42.onrender.com
