from fastapi import APIRouter

from db.init.initial_data import insert_initial_data

router = APIRouter(
    prefix="/admin"
)


@router.post("/initialize-data", tags=["admin"])
def initialize_data():
    insert_initial_data()
    return "Initial data created"
