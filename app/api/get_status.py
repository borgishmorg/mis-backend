from app.settings import settings

def get_status():
    return {
        'host': settings.HOST,
        'alive': True
    }
