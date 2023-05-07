import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from app.db.table import Churn


class Counts:
    def __init__(self):
        print(os.path.abspath('.'))
        self.engine = create_engine(f"sqlite:///app/db/churn.db")

    @staticmethod
    def columns(col_type: str = None):
        if col_type:
            return [
                col.name
                for col in Churn.__table__.c
                if col.type.python_type.__name__ == col_type
            ]
        return [col.name for col in Churn.__table__.c]

    def column_values(self, column_name: str):
        with Session(self.engine) as s:
            result = s.query(getattr(Churn, column_name)).distinct().all()
            s.close()

            return {"values": [value[0] for value in result]}

    def user_counts(self):
        with Session(self.engine) as s:
            result = s.query(Churn.customerID).count()
            s.close()

            return {"Customer Count": result}

    def categorical_distribution(self, column_name: str):
        with Session(self.engine) as s:
            result = (
                s.query(getattr(Churn, column_name), func.count(Churn.customerID))
                .group_by(getattr(Churn, column_name))
                .all()
            )
            s.close()
            return {key: value for key, value in result}

    def numerical_distribution(self, column_name: str):
        with Session(self.engine) as s:
            result = s.query(
                func.count(getattr(Churn, column_name)),
                func.round(func.sum(getattr(Churn, column_name))),
                func.round(func.avg(getattr(Churn, column_name))),
            ).first()
            s.close()
            return {key: value for key, value in zip(["Count", "Sum", "Avg"], result)}
