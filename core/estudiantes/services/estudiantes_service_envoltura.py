from api.payloads.request import EstudianteRequest, EstudianteActualizarRequest;
from api.payloads.response import Response
from config.basededatos import BaseDeDatos
from bson import ObjectId

basededatos = BaseDeDatos()
engine = basededatos.obtener_conexion()

def agregar_estudiante_detalle(estudiante: EstudianteRequest):
    mydb = engine["uniminuto"]
    mycol = mydb["estudiantes"]
    estudiante = {
        "tipo_identificacion" : estudiante.tipo_identificacion,
        "documento_identificacion" : estudiante.documento_identificacion,
        "nombres" : estudiante.nombres,
        "apellidos" : estudiante.apellidos,
        "genero" : estudiante.genero,
        'telefono' : estudiante.telefono,
        'email' : estudiante.email,
        'direccion' : estudiante.direccion
    }
    resultado = mycol.insert_one(estudiante)
    data = {"nombre": estudiante.nombre}
    return Response(data, 200, "El estudiante fue agregado satisfactoriamente.", False)

def leer_estudiante_detalle(documento_identidad: str):
    mydb = engine["uniminuto"]
    mycol = mydb["estudiantes"]
    filtros_estudiante= {
        "documento_identificacion" : documento_identidad
    }
    
    cursor = mycol.find(filtros_estudiante).limit(1)
    for item in cursor:
        estudiante = {"_id" : str(item["_id"]),
            "nombres" : item["nombres"],
            "apellidos" : item["apellidos"], 
            "documento_identificacion" : item["documento_identificacion"],
            "telefono" : item["telefono"],
            "email" : item["email"],
            "direccion" : item["direccion"],
            "genero" : item["genero"]
        };
    return estudiante;

def actualizar_estudiante_detalle(estudiante_actualizar_req : EstudianteActualizarRequest, documento_identidad: str):
    mydb = engine["uniminuto"]
    mycol = mydb["estudiantes"]
    filtros_estudiante = {
        "documento_identificacion" : documento_identidad
    }
    print(f"Documento identidad: {documento_identidad}")
    print(f"nombres: {estudiante_actualizar_req.nombres}")
    print(f"apellidos: {estudiante_actualizar_req.apellidos}")
    valores_nuevos = { "$set": { "nombres": estudiante_actualizar_req.nombres, 
                                "apellidos" : estudiante_actualizar_req.apellidos,
                                "genero" : estudiante_actualizar_req.genero,
                                "direccion" : estudiante_actualizar_req.direccion } }
    print(estudiante_actualizar_req.direccion)
    resultado = mycol.update_one(filtros_estudiante, valores_nuevos)
    respuesta_mensaje = "El estudiante fue actualizado satisfactoriamente";
    response_code = 200;
    data = { "nombre": estudiante_actualizar_req.nombre }
    error = False
    if (resultado.modified_count == 0) :
        respuesta_mensaje = "El estudiante no fue actualizado. El estudiante no fue encontrado con el id " +  str(id_estudiante);
        error = True;
        data = None;
    return Response(data, response_code, respuesta_mensaje, error);


def eliminar_estudiante_detalle(documento_identidad : str):
    mydb = engine["uniminuto"]
    mycol = mydb["estudiantes"]
    filtros_estudiante = {
        "documento_identificacion" : documento_identidad
    }
    resultado = mycol.delete_one(filtros_estudiante)
    if resultado.deleted_count == 1:
        response_msg = "El estudiante fue eliminado satisfactoriamente";
        response_code = 200;
        error = False;
    else:
        response_msg = "Error eliminando un estudiante";
        response_code = 500;
        error = True;
    data = {"documento_identidad" : documento_identidad};
    return Response(resultado, response_code, response_msg, error);

def leer_todos_estudiantes_detalle():
    mydb = engine["uniminuto"]
    mycol = mydb["estudiantes"]
    cursor = mycol.find(); 
    datos = []
    for item in cursor:
        print(type(item["_id"]));
        datos.append({
            "_id" : str(item["_id"]),
            "nombres" : item["nombres"],
            "apellidos" : item["apellidos"], 
            "documento_identificacion" : item["documento_identificacion"],
            "telefono" : item["telefono"],
            "email" : item["email"],
            "direccion" : item["direccion"],
            "genero" : item["genero"],
        })

    return Response(datos, 200, "Los estudiantes son recuperados satisfactoriamente", False);
