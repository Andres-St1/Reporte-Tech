from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
from database import SessionLocal, engine

# Crear las tablas automáticamente en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Habilitar acceso desde cualquier origen (útil para conectar Appsmith luego)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión con base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta base para probar
@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a Security Tech - API de Reportes!"}

# Crear nuevo reporte
@app.post("/reportes", response_model=schemas.ReporteOut)
def crear_reporte(reporte: schemas.ReporteCreate, db: Session = Depends(get_db)):
    nuevo = models.Reporte(**reporte.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar todos los reportes
@app.get("/reportes", response_model=list[schemas.ReporteOut])
def listar_reportes(db: Session = Depends(get_db)):
    return db.query(models.Reporte).all()
