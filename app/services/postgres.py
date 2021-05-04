from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.settings import settings


engine = create_engine(
    settings.POSTGRES_DSN, 
    echo=settings.ENABLE_DEVELOP_MOD,
    future=True
)
session_maker = sessionmaker(
    bind=engine, 
    autoflush=True,
    # class_=AsyncSession,
    # autocommit=True,
)


@contextmanager
def session_scope():
    session: Session = session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
