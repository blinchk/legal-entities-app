import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from db.base import Base
from db.database import engine
from routes import legal_entity, admin

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(legal_entity.router)
app.include_router(admin.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.exception_handler(ValueError)
def handle_value_error(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "message": exc.args[0] if exc.args[0] is not None else "Bad Request Exception"
        }
    )


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
