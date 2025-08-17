from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engin = create_async_engine(url = 'sqlite+aiosqlite:///base.db')

new_session = async_sessionmaker(bind=engin, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class TaskModel(Base):
    __tablename__ = 'task'
    
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    discription : Mapped[str|None]
    
async def create_table():
    async with engin.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_table():
    async with engin.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)