from typing import List
import sqlalchemy
from sqlalchemy import inspect, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, as_declarative
# from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi import FastAPI, Depends
from pydantic import BaseModel


# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite+aiosqlite:///test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_async_engine(
    DATABASE_URL, 
    echo=True
)
async_session_maker = sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    # autocommit=True,
    # autoflush=True
)

@as_declarative()
class Base:
    def dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

def async_session() -> AsyncSession:
    return async_session_maker()

class NoteDB(Base):
    __tablename__ = 'notes'

    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    text = sqlalchemy.Column("text", sqlalchemy.String)
    completed = sqlalchemy.Column("completed", sqlalchemy.Boolean)


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    pass


@app.get("/notes/", response_model=List[Note])
async def read_notes(
    session: AsyncSession = Depends(async_session)
) -> List[Note]:
    notes = list()
    async with session.begin():
        results = await session.execute(select(NoteDB).order_by(NoteDB.id))
        for note, in results.all():
            notes.append(note.dict())
    return notes


@app.post("/notes/", response_model=Note)
async def create_note(
    note: NoteIn,
    session: AsyncSession = Depends(async_session)
) -> Note:
    note = NoteDB(**note.dict())
    async with session.begin():
        session.add(note)
        await session.flush()
        return note.dict()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0')
