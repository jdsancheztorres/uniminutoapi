from fastapi import FastAPI
from api.api import router as api_router

estudiante_api= FastAPI();
estudiante_api.include_router(api_router)
#http://localhost:9999/docs
#python3 -m uvicorn main:estudiante_api --reload --port 9999