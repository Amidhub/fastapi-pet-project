from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from schema import TaskAddSchema, TaskSchema, TaskIdSchema
from repository import TaskRepository
router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.get('')
async def read_tasks() -> list[TaskSchema]:
    tasks = await TaskRepository.find_all()
    return tasks

@router.post('')
async def write_tasks(task : Annotated[TaskAddSchema, Depends()]) -> TaskIdSchema: # Schema + Depend = автоматическое преобразование json в dict
    task_id = await TaskRepository.add_one(task)
    
    
    return {'ok' : True, 'task_id' : task_id}