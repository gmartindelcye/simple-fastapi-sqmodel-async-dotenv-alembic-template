from typing import Optional

from sqlmodel import SQLModel, Field


class DataMOdel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    artist: str
    year: Optional[int] = None

