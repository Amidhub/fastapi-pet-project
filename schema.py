from pydantic import BaseModel, ConfigDict

class TaskAddSchema(BaseModel):
    name : str
    discription : str | None = None

class TaskSchema(TaskAddSchema):
    id : int
    model_config = ConfigDict(from_attributes=True)
class TaskIdSchema(BaseModel):
    ok : bool = True
    task_id : int 