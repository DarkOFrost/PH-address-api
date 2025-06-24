from fastapi import FastAPI, Query
from sqlmodel import Session, select, create_engine
from models import Region, Province, Barangay

app = FastAPI()
engine = create_engine("sqlite:///database.db")

@app.get("/regions")
def get_regions():
    with Session(engine) as session:
        regions = session.exec(select(Region)).all()
        return regions

@app.get("/provinces")
def get_provinces(region_code: str = Query(...)):
    with Session(engine) as session:
        provinces = session.exec(select(Province).where(Province.regCode == region_code)).all()
        return provinces

@app.get("/barangays")
def get_barangays(province_code: str = Query(...)):
    with Session(engine) as session:
        barangays = session.exec(select(Barangay).where(Barangay.provCode == province_code)).all()
        return barangays
