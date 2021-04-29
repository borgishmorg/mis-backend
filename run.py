import uvicorn
from app import app, settings

if __name__ == '__main__':
    uvicorn.run(
        'app:app', 
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.WORKERS,
        reload=settings.ENABLE_AUTORELOAD
    )
