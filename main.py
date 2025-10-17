from datetime import datetime, timezone
from fastapi import FastAPI

from app.config import settings
from app.schema import Profile
from app.catfact import cat_fact

app = FastAPI()


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
    my_info['fact'] = cat_fact(settings.URL)
    return my_info
