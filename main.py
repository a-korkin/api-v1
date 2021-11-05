import uvicorn
from fastapi import FastAPI
from routers.api import api_router
from core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None
    )
    app.include_router(api_router, prefix=settings.API_V1)

    return app

app = create_app()    

def main():    
    uvicorn.run(app="main:app", port=5000, reload=True)

if __name__ == "__main__":
    main()