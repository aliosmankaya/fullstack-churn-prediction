from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Churn API")


@app.get("/hello")
def hello_world():
    return JSONResponse(
        status_code=200,
        content="Welcome the Churn API!"
    )
