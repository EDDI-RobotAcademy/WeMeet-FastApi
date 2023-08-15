from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

origins = os.getenv('origins')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # *별 찍으면 안됨! 전부다 허용하겠다는 이야기라
    allow_credentials=True,
    allow_methods=["*"],  # *은 전부다
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
