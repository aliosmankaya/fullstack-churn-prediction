from pydantic import BaseModel, Field, validator
from fastapi.exceptions import HTTPException

from app.services.counts import Counts


class ColumnsSchema(BaseModel):
    col_type: str = Field(None)

    @validator("col_type")
    def col_type_must_be_in(cls, v):
        col_type_list = [None, "str", "int"]
        if v not in col_type_list:
            raise HTTPException(
                status_code=400, detail=f"col_type must be in {col_type_list}"
            )
        return v


class ColumnValuesSchema(BaseModel):
    column_name: str = Field(...)

    @validator("column_name")
    def column_name_must_be_in(cls, v):
        column_name_list = Counts().columns(col_type="str")
        if v not in column_name_list:
            raise HTTPException(
                status_code=400, detail=f"column_name must be in {column_name_list}"
            )
        return v


class CategoricalDistSchema(BaseModel):
    column_name: str = Field(...)

    @validator("column_name")
    def column_name_must_be_in(cls, v):
        column_name_list = Counts().columns(col_type="str")
        if v not in column_name_list:
            raise HTTPException(
                status_code=400, detail=f"column_name must be in {column_name_list}"
            )
        return v


class NumericalDistSchema(BaseModel):
    column_name: str = Field(...)

    @validator("column_name")
    def column_name_must_be_in(cls, v):
        column_name_list = Counts().columns(col_type="int")
        if v not in column_name_list:
            raise HTTPException(
                status_code=400, detail=f"column_name must be in {column_name_list}"
            )
        return v
