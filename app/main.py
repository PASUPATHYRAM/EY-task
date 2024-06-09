from fastapi import FastAPI
import uvicorn
from app.dbsetup.setup import engine,session,Base
from app.routes.pay_load import pay_load


def run_app():
    app=FastAPI(title="EY_TASK")
    Base.metadata.create_all(bind=engine)
    app.include_router(pay_load)
    return app





if __name__=="__main__":
    uvicorn.run("main:run_app",host="0.0.0.0",port=9990)
