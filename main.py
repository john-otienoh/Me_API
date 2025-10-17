from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from app.schema import Profile
from app.catfact import cat_fact

app = FastAPI()
URL = "https://catfact.ninja/fact"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



my_info = {
    "status": "Success",
    "user": {
        "email": "johnteclaire@gmail.com",
        "name": "John Charles Otienoh",
        "stack": "Python/fastAPI"
    },
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "fact": ""
}

@app.get("/me", response_model=Profile)
async def get_my_info():
    "Retreive Basic information"
    my_info['fact'] = cat_fact(URL)
    return my_info
