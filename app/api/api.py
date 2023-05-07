from fastapi import FastAPI, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.schema.counts import (
    ColumnsSchema,
    ColumnValuesSchema,
    CategoricalDistSchema,
    NumericalDistSchema,
)
from app.services.counts import Counts
from app.services.predict import predict_service

router = FastAPI(title="Churn API")


@router.get("/columns")
def columns(col_type=Depends(ColumnsSchema)):
    try:
        return JSONResponse(
            status_code=200, content=Counts().columns(col_type=col_type.col_type)
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@router.get("/column-values")
def column_values(column_name=Depends(ColumnValuesSchema)):
    try:
        return JSONResponse(
            status_code=200,
            content=Counts().column_values(column_name=column_name.column_name),
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@router.get("/customer-count")
def customer_count():
    try:
        return JSONResponse(status_code=200, content=Counts().user_counts())
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@router.get("/categorical-distribution")
def categorical_distribution(column_name=Depends(CategoricalDistSchema)):
    try:
        return JSONResponse(
            status_code=200,
            content=Counts().categorical_distribution(
                column_name=column_name.column_name
            ),
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@router.get("/numerical-distribution")
def numerical_distribution(column_name=Depends(NumericalDistSchema)):
    try:
        return JSONResponse(
            status_code=200,
            content=Counts().numerical_distribution(
                column_name=column_name.column_name
            ),
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.size > 2 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        file_ = await file.read()
        return predict_service(file_)
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})
