from pydantic import BaseModel

class PropertyQuery(BaseModel):
    city: str
    min_price: int
    max_price: int


class PropertyResponse(BaseModel):
    Id: int
    ArchitecturalStyle: str
    StructureType: str
    subType: str
    BedroomCount: int
    BathroomCount: int
    ListPrice: int
    Address_City: str
    ParkingTotal: str 
    YearBuilt: int
    LivingAreaSquareFeet: int

 