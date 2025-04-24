from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    tecnico = Column(String)
    ubicacion = Column(String)
    tipo = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)
    descripcion = Column(String)
