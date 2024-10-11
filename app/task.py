from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.get("/")
async def all_tasks():
    pass  # Возвращаем все задачи

@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass  # Возвращаем задачу по ID

@router.post("/create")
async def create_task():
    pass  # Создаем новую задачу

@router.put("/update")
async def update_task():
    pass  # Обновляем задачу

@router.delete("/delete")
async def delete_task():
    pass  # Удаляем задачу
