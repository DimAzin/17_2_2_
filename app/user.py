from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
async def all_users():
    pass  # Возвращаем всех пользователей

@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass  # Возвращаем пользователя по ID

@router.post("/create")
async def create_user():
    pass  # Создаем нового пользователя

@router.put("/update")
async def update_user():
    pass  # Обновляем пользователя

@router.delete("/delete")
async def delete_user():
    pass  # Удаляем пользователя
