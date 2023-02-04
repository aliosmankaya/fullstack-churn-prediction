from fastapi import FastAPI
from fastapi.responses import JSONResponse

from ..controller.counts import (
    columns_controller,
    column_values_controller,
    user_counts_controller,
    categorical_distribution_controller,
    numerical_distribution_controller,
)

app = FastAPI(title="Churn API")


@app.get("/columns")
def columns(col_type: str):
    try:
        return JSONResponse(
            status_code=200, content=columns_controller(col_type=col_type)
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@app.get("/column-values")
def columns(column: str):
    try:
        return JSONResponse(
            status_code=200, content=column_values_controller(column=column)
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@app.get("/customer-count")
def customer_count():
    try:
        return JSONResponse(status_code=200, content=user_counts_controller())
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@app.get("/categorical-distribution")
def categorical_distribution(column: str):
    try:
        return JSONResponse(
            status_code=200,
            content=categorical_distribution_controller(column=column),
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})


@app.get("/numerical-distribution")
def numerical_distribution(column: str):
    try:
        return JSONResponse(
            status_code=200, content=numerical_distribution_controller(column=column)
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"Error!", e})
