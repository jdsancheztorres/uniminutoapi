from fastapi import APIRouter
from api.estudiantes import estudiante;

router = APIRouter()
router.include_router(estudiante.router)