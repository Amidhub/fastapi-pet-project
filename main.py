from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import delete_table, create_table
from router import router as main_router


@asynccontextmanager
async def lifespan(app : FastAPI):
    await delete_table()
    print('the table is droped')
    await create_table()
    print('the table is created')
    yield
    print('Off table')

app = FastAPI(lifespan=lifespan)


app.include_router(main_router)



