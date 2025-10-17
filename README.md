# Stage 0: Dynamic Profile Endpoint

## 🚀 Overview

This project is my submission for Backend Wizards Stage 0, which involves building a simple RESTful API that returns profile information and a random cat fact fetched dynamically from the Cat Facts API.</br>
The endpoint returns real-time data, demonstrating the use of:

- RESTful API design
- JSON response formatting
- Third-party API consumption
- Dynamic timestamps
- Error handling & fallback logic

## ✨ Features

✅ /me endpoint that returns:

- Profile information (name, email, stack)
- Random cat fact (via Cat Facts API)
- Dynamic UTC timestamp in ISO 8601 format

✅ Proper JSON structure and headers </br>
✅ Graceful error handling (fallback fact)</br>
✅ Clean code and modular architecture</br>
✅ Environment variable configuration</br>
✅ CORS and request logging middleware</br>

## Tech Stack

| Component         | Technology                                     |
| ----------------- | ---------------------------------------------- |
| Language          | **Python 3.10+**                               |
| Framework         | **FastAPI**                                    |
| HTTP Client       | **httpx** (for async API calls)                |
| Deployment        | **Railway / Fly.io / Heroku / PXXL App / AWS** |
| Config Management | **python-dotenv**                              |
| Server            | **Uvicorn**                                    |

## Project structure

```bash
ME_API/
│
├── main.py                       # Application entry point
│
├── requirements.txt               # Project dependencies
│
├── app/
│   ├── routes/
│   │   └── profile.py             # /me endpoint route
│   │
│   ├── services/
│   │   └── catfacts_service.py    # Cat Facts API logic
│   │
│   ├── core/
│   │   ├── config.py              # Environment and settings
│   │   ├── utils.py               # Timestamp & helper functions
│   │   └── logger.py              # Logging setup
│   │
│   └── schemas/
│       └── response_schema.py     # Pydantic model for response
│
├── .env                           # Environment variables
├── .gitignore                     # Ignored files
└── README.md                      # Project documentation
```

## Installation Setup

Clone the repository

```bash
git clone https://github.com/<your-username>/ME_API.git
cd ME_API
```

Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```bash
cp .env.example .env
```

Running the server

```bash
uvicorn main:app --reload
```

Visit

```bash
http://localhost:8000/me
```

## API Documentation

Endpoint

```vbnet
GET /me
```

Headers

```pgsql
Content-Type: application/json
```

Response Format

```json
{
  "status": "success",
  "user": {
    "email": "johndoe@example.com",
    "name": "John Doe",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T09:40:00Z",
  "fact": "Cats sleep 70% of their lives."
}
```

Error Handling - If the Cat Facts API fails or times out, the endpoint returns a fallback message.

```json
{
  "status": "success",
  "user": {
    "email": "johndoe@example.com",
    "name": "John Doe",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T09:40:00Z",
  "fact": "Could not fetch cat fact at the moment."
}
```

Verify:

- Response code → 200 OK
- Content-Type → application/json
- Timestamp updates dynamically
- Cat fact changes each request
