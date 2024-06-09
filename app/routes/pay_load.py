from fastapi import FastAPI, APIRouter,Depends
from typing import Dict,List
from app.schemas.dataschema import PayloadRequest,PayloadResponse,PayloadResponses
from app.dbsetup.dbconfig import get_db
from sqlalchemy.orm import session
from app.service.logic import addlogic,getdata,getdata_by_id

pay_load=APIRouter(prefix='/payload',tags=['Payload'])

@pay_load.post('/adddata', response_model=Dict)
def add_data(data: PayloadRequest, db: session = Depends(get_db)):
    if data is None:
        raise ValueError("Invalid request")
    else:
        data_response = PayloadResponse(**data.dict())
        return addlogic(data_response, db)

@pay_load.get('/all',response_model=List[PayloadResponses])
def get_data(db:session=Depends(get_db)):
    return getdata(db)

@pay_load.get('/batch/{id}',response_model=List[PayloadResponses])
def get_batch_data_by_id(id:str,db:session=Depends(get_db)):
    return getdata_by_id(id,db)


