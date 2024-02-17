from fastapi import APIRouter;
from core.estudiantes.services.estudiantes_service import *;
from api.payloads.request import EstudianteRequest, EstudianteActualizarRequest;

router = APIRouter(
    prefix="/api/v1/estudiantes",
    tags=["Estudiantes - Jose Danilo Sanchez Torres"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_description="Agregar estudiante")
async def agregar_estudiante(estudiante: EstudianteRequest):
    response = None;
    try:
        response = await agregar_estudiante_serv(estudiante);
    except Exception as ex:
        print(ex)
        response = "El estudiante con id " + str(estudiante.nombres) + " no fue encontrado";

    return response;

@router.put("/{documento_identidad}")
async def actualizar_estudiante(estudiante_actualizar_req : EstudianteActualizarRequest, documento_identidad: str):
    response_message = "El estudiante fue recuperado satisfactoriamente"
    data = None;
    error = True;
    try:
        response = await actualizar_estudiante_serv(estudiante_actualizar_req, documento_identidad);
    except Exception as ex:
        response = Response(data, 500, "Error al actualizar un producto: " + str(ex), error);

    return response;

@router.delete("/{documento_identidad}")
async def eliminar_estudiante(documento_identidad : str):
    data = None;
    error = True;
    try:
        response = await eliminar_estudiante_serv(documento_identidad);
    except Exception as ex:
        response = Response(data, 500, "Error al eliminar un estudiante: " + str(ex), error);

    return response;

@router.get("/")
async def leer_todos_estudiantes():
    return leer_todos_estudiantes_detalle();

@router.get("/{documento_identidad}")
async def leer_estudiante(documento_identidad: str):
    response_message = "El estudiante fue recuperado satisfactoriamente"
    response= None;
    error = True;
    http = 200;
    try:
        response = await leer_estudiante_serv(documento_identidad);
    except Exception as ex:
        print(ex)
        response_message = "El estudiante con id " + str(documento_identidad) + " no fue encontrado";

    return response
