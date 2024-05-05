from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/explorer")

@router.get("/")
def top():
    return JSONResponse("Top explorer router!", status_code=200)