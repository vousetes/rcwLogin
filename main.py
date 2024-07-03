
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()
# Allow oreigins

origins =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Name( BaseModel):
    first_name : str
    last_name : str

app.post('/login')
async def welcome(name: Name):
    return {f"Request confirmation: Welcome {name.first_name}, {name.last_name}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
