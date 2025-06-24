import json
from sqlmodel import Session, SQLModel, create_engine
from models import Region, Province, Barangay

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    with open("refregion.json") as f:
        regions = json.load(f)["RECORDS"]
        session.add_all([Region(**r) for r in regions])

    with open("refprovince.json") as f:
        provinces = json.load(f)["RECORDS"]
        session.add_all([Province(**p) for p in provinces])

    with open("refbrgy.json") as f:
        barangays = json.load(f)["RECORDS"]
        session.add_all([Barangay(**b) for b in barangays])

    session.commit()
