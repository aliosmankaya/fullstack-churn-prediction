import os
import sqlite3
import pandas as pd


def data_dump():
    # Data Process
    df = pd.read_parquet(os.path.abspath(".") + "/data/churn.parquet")
    df.SeniorCitizen = df.SeniorCitizen.astype("object")
    df.loc[df.TotalCharges == " ", "TotalCharges"] = 0
    df.TotalCharges = df.TotalCharges.astype("float64")

    # Query
    query = """
        CREATE TABLE IF NOT EXISTS churn (
            customerID VARCHAR NOT NULL,
            gender VARCHAR NOT NULL,
            SeniorCitizen INTEGER NOT NULL,
            Partner VARCHAR NOT NULL,
            Dependents VARCHAR NOT NULL,
            tenure INTEGER NOT NULL,
            PhoneService VARCHAR NOT NULL,
            MultipleLines VARCHAR NOT NULL,
            InternetServices VARCHAR NOT NULL,
            OnlineSecurity VARCHAR NOT NULL,
            OnlineBackup VARCHAR NOT NULL,
            DeviceProtection VARCHAR NOT NULL,
            TechSupport VARCHAR NOT NULL,
            StreamingTV VARCHAR NOT NULL,
            StreamingMovies VARCHAR NOT NULL,
            Contract VARCHAR NOT NULL,
            PaperlessBilling VARCHAR NOT NULL,
            PaymentMethod VARCHAR NOT NULL,
            MonthlyCharges INTEGER NOT NULL,
            TotalCharges INTEGER NOT NULL,
            Churn VARCHAR NOT NULL
        )
    """

    # Connection & Insertion
    connection = sqlite3.connect(os.path.abspath(".") + "/app/db/churn.db")
    connection.execute(query)
    df.to_sql(name="churn", con=connection, if_exists="replace", index=False)
    connection.commit()
    connection.close()

    return True
