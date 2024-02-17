from fastapi import FastAPI
from api.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware

estudiante_api= FastAPI();
estudiante_api.include_router(api_router)
estudiante_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#http://localhost:9999/docs
#python3 -m uvicorn main:estudiante_api --reload --port 9999
