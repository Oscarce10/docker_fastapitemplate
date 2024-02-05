from fastapi import APIRouter
from starlette.responses import JSONResponse


router = APIRouter()


@router.get("/", tags=["root"])
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "API is ready",
            "data": {
                "owner": "NAME",
                "source": "https://github.com/USERNAME/REPO",
            }
        }
    )


@router.get("/health", tags=["healthcheck"])
async def get_health():
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "OK"
        }
    )
