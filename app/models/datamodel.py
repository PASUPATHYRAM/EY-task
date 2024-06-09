from app.dbsetup.setup import Base
from sqlalchemy import Integer,Column,String,DateTime,func


class DataModel(Base):
    __tablename__="payload"
    batchid = Column(String, primary_key=True)
    payload = Column(String, nullable=False)
    status = Column(String, default='Completed')
    started_at = Column(DateTime, default=func.now())
    completed_at = Column(DateTime, default=func.now(),onupdate=func.now())

