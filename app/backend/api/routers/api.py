from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def begin():
    return {"hello": "world"}