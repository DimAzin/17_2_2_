from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# движок
DATABASE_URL = "sqlite:///taskmanager.db"

engine = create_engine(DATABASE_URL, echo=True)

# фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()
