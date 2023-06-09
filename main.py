from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session

# Import from models the corrsponding Database Classes
#from models import DataModel

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/datamodels", response_model=list[DataModel])
async def get_DataModel(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(DataModel))
    DataModel = result.scalars().all()
    return [DataModel(dataproperty1=DataModel.dataproperty1, dataproperty2=DataModel.dataproperty2, id=DataModel.id) for DataModel in DataModel]


@app.post("/datamodels")
async def add_DataModel(DataModel: DataModel, session: AsyncSession = Depends(get_session)):
    DataModel = DataModel(dataproperty1=DataModel.dataproperty1, dataproperty1=DataModel.dataproperty1)
    session.add(DataModel)
    await session.commit()
    await session.refresh(DataModel)
    return DataModel