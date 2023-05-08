import io
import os
import mlflow
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse

from app.db.table import Churn


def predict_service(file):
    # Load
    abs_path = os.path.abspath("..")
    model = mlflow.pyfunc.load_model(
        abs_path + "/notebook/mlruns/1/39d2c9fc6f184aa187a2bd09ade6a9a3/artifacts/model"
    )
    df = pd.read_csv(io.BytesIO(file))

    # Validation
    default_columns = [col.name for col in Churn.__table__.c if col.name != "Churn"]
    if sorted(df.columns.tolist()) != sorted(default_columns):
        raise HTTPException(
            status_code=400,
            detail=f"File columns must be equal to {sorted(default_columns)}",
        )

    # Preprocess
    df.SeniorCitizen = df.SeniorCitizen.astype("object")
    df.loc[df.TotalCharges == " ", "TotalCharges"] = 0
    df.TotalCharges = df.TotalCharges.astype("float64")
    customer_id = df["customerID"]
    df.drop("customerID", axis=1, inplace=True)
    le = LabelEncoder()
    for col in df.columns.tolist():
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])
        else:
            pass

    # Prediction
    prediction = model.predict(df)

    # Export
    prediction = pd.DataFrame(data={"customerID": customer_id, "Churn": prediction})
    stream = io.StringIO()
    prediction.to_csv(stream, index=False, header=True, sep=",", decimal=".")
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=predictions.csv"

    return response
