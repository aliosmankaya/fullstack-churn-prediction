import uvicorn
from app.api.api import router


if __name__ == "__main__":
    uvicorn.run(app=router, host="0.0.0.0", port=8000)
