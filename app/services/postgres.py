from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.settings import settings


engine = create_engine(
    settings.POSTGRES_DSN, 
    echo=settings.ENABLE_DEVELOP_MOD
)
session_maker = sessionmaker(
    bind=engine, 
    # class_=AsyncSession,
    # autocommit=True,
    # autoflush=True
)


def session() -> Session:
    return session_maker()
