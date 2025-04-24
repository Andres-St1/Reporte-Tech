from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PEGA AQUÍ tu conexión de Render
DATABASE_URL = "postgresql://bd_reporte_tech_user:XFIDy10azf9h2NzCpQ0WM0IScJpfWUgK@dpg-d059psp5pdvs73etsdvg-a.ohio-postgres.render.com/bd_reporte_tech"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
