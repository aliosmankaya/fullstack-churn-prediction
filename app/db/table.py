from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Churn(Base):
    __tablename__ = "churn"

    customerID = Column(String, nullable=False, primary_key=True)
    gender = Column(String, nullable=False)
    SeniorCitizen = Column(Integer, nullable=False)
    Partner = Column(String, nullable=False)
    Dependents = Column(String, nullable=False)
    tenure = Column(Integer, nullable=False)
    PhoneService = Column(String, nullable=False)
    MultipleLines = Column(String, nullable=False)
    InternetService = Column(String, nullable=False)
    OnlineSecurity = Column(String, nullable=False)
    OnlineBackup = Column(String, nullable=False)
    DeviceProtection = Column(String, nullable=False)
    TechSupport = Column(String, nullable=False)
    StreamingTV = Column(String, nullable=False)
    StreamingMovies = Column(String, nullable=False)
    Contract = Column(String, nullable=False)
    PaperlessBilling = Column(String, nullable=False)
    PaymentMethod = Column(String, nullable=False)
    MonthlyCharges = Column(Integer, nullable=False)
    TotalCharges = Column(Integer, nullable=False)
    Churn = Column(String, nullable=False)
