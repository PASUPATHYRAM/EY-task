from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


url="sqlite:///C:/Pasupathy/Python/EY-task/app/dbsetup/database.db"


engine=create_engine(url=url)
session=sessionmaker(bind=engine,autoflush=False)
Base=declarative_base()


