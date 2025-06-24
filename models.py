from sqlmodel import SQLModel, Field

class Region(SQLModel, table=True):
    id: int = Field(primary_key=True)
    psgcCode: str
    regDesc: str
    regCode: str

class Province(SQLModel, table=True):
    id: int = Field(primary_key=True)
    psgcCode: str
    provDesc: str
    regCode: str
    provCode: str

class Barangay(SQLModel, table=True):
    id: int = Field(primary_key=True)
    psgcCode: str
    brgyDesc: str
    regCode: str
    provCode: str
    citymunCode: str
    brgyCode: str
