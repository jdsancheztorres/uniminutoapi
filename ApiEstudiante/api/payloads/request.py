from pydantic import BaseModel, Field
from typing import Optional

class EstudianteRequest(BaseModel):
    
    tipo_identificacion: str = Field(
        None, title="Tipo de Identificación del Estudiante", max_length=100
    )
    documento_identificacion: str = Field(
        None, title="Documentacion de Identificación del Estudiante", max_length=100
    )
    nombres: str = Field(
        None, title="Nombre del Estudiante", max_length=100
    )
    apellidos: str = Field(
        None, title="Apellido del Estudiante", max_length=100
    )
    genero: str = Field(
        None, title="Genero del Estudiante", max_length=100
    )
    email: str = Field(
        None, title="Genero del Estudiante", max_length=100
    )
    direccion: str = Field(
        None, title="Direccion del Estudiante", max_length=100
    )
    telefono: str = Field(
        None, title="Telefono del Estudiante", max_length=100
    )

class EstudianteActualizarRequest(BaseModel):
    id_estudiante : str = Field(
        None, title="Id estudiante a modificar", max_length=1000
    )
    tipo_identificacion: str = Field(
        None, title="Tipo de Identificación del Estudiante", max_length=100
    )
    documento_identificacion: str = Field(
        None, title="Documentacion de Identificación del Estudiante", max_length=100
    )
    nombres: str = Field(
        None, title="Nombre del Estudiante", max_length=100
    )
    apellidos: str = Field(
        None, title="Apellido del Estudiante", max_length=100
    )
    genero: str = Field(
        None, title="Genero del Estudiante", max_length=100
    )
    email: str = Field(
        None, title="Genero del Estudiante", max_length=100
    )
    direccion: str = Field(
        None, title="Direccion del Estudiante", max_length=100
    )
