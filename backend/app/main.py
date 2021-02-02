import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routers.calculator import calculator_router
from app.core import config

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1")
async def root():
    return {"message": "api root page"}


# Routers
app.include_router(calculator_router, prefix="/api/v1", tags=["calculator"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
