from sqlalchemy.orm import session
from app.schemas.dataschema import PayloadRequest,PayloadResponse,PayloadResponses
from app.models.datamodel import DataModel
from app.utils.helper import *
from fastapi import HTTPException







def addlogic(data: PayloadResponse, db: session):
    add_data = data.dict()
    print(add_data['data_compute'])
    new_data = helper_toconvert_add(add_data['data_compute'])
    print(new_data)
    existing_record = db.query(DataModel).filter(DataModel.batchid == add_data['batchid']).first()
    if existing_record is not None:
        return {'Message': f"A record with batchid {add_data['batchid']} already exists."}

    add = DataModel(batchid=add_data['batchid'], payload=new_data)
    db.add(add)
    db.commit()
    db.refresh(add)
    return {'Message': "Data Added successfully"}

def getdata(db: session):
    data = db.query(DataModel).all()
    responses = []
    for rec in data:
        data_com = str_int(rec.payload)
        r_data = PayloadResponses(batchid=rec.batchid, response=data_com, status=rec.status,
                                  started_at=rec.started_at, completed_at=rec.completed_at)
        responses.append(r_data)
    return responses

def getdata_by_id(id:str,db:session):
    data=db.query(DataModel).filter(DataModel.batchid==id).first()

    if data:
        data_com = str_int(data.payload)
        r_data = PayloadResponses(batchid=data.batchid, response=data_com, status=data.status,
                                  started_at=data.started_at, completed_at=data.completed_at)

        return [r_data]
    else:
        raise HTTPException(status_code=404,detail="ID not exists")
