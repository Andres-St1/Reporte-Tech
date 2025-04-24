from pydantic import BaseModel
from datetime import datetime

class ReporteCreate(BaseModel):
    tecnico: str
    ubicacion: str
    tipo: str
    descripcion: str

class ReporteOut(ReporteCreate):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
