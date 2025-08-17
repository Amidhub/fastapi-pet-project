from database import new_session
from schema import TaskAddSchema, TaskSchema
from database import TaskModel
from sqlalchemy import select
class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAddSchema) -> int:
        async with new_session() as session:
            data_dict = data.model_dump()
            
            task = TaskModel(**data_dict)
            
            session.add(task)
            await session.flush()
            await session.commit()
            
            return task.id
    
    @classmethod
    async def find_all(cls) -> list[TaskSchema]:
        async with new_session() as session:
            query = select(TaskModel)
            res = await session.execute(query)
            tasks = res.scalars().all()
            tasks = [TaskSchema.model_validate(task) for task in tasks]
            return tasks