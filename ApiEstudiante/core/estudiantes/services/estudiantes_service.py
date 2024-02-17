from core.estudiantes.services.estudiantes_service_envoltura import *;
from api.payloads.request import EstudianteRequest, EstudianteActualizarRequest;

async def agregar_estudiante_serv(estudiante: EstudianteRequest):
    response = None;
    try:
        response = agregar_estudiante_detalle(estudiante);
    except Exception as ex:
        print(ex)
        response = "El estudiante  " + str(estudiante.nombres) + " no fue encontrado";

    return response;

async def actualizar_estudiante_serv(estudiante_actualizar_req : EstudianteActualizarRequest, documento_identidad: str):
    response_message = "El estudiante fue recuperado satisfactoriamente"
    data = None;
    error = True;
    try:
        response = actualizar_estudiante_detalle(estudiante_actualizar_req, documento_identidad);
    except Exception as ex:
        response = Response(data, 500, "Error al actualizar un estudiante: " + str(ex), error);

    return response;

async def eliminar_estudiante_serv(documento_identidad : str):
    data = None;
    error = True;
    try:
        response = eliminar_estudiante_detalle(documento_identidad);
    except Exception as ex:
        response = Response(data, 500, "Error al eliminar un estudiante: " + str(ex), error);

    return response;

async def leer_todos_estudiantes_serv():
    return leer_todos_estudiantes_serv();

async def leer_estudiante_serv(documento_identidad : str):
    response_message = "El estudiante fue recuperado satisfactoriamente"
    data = None;
    error = True;
    http = 200;
    try:
        data = leer_estudiante_detalle(documento_identidad);
    except Exception as ex:
        print(ex)
        response_message = "*** El estudiante con id " + str(documento_identidad) + " no fue encontrado";

    return Response(data, http, response_message, error)