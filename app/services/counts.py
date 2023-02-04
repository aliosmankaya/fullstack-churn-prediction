import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from ..db.schema import Churn


class Counts:
    def __init__(self):
        self.engine = create_engine(f"sqlite:////{os.path.abspath('.')}/db/churn.db")

    @staticmethod
    def columns(col_type: str):
        return [
            col.name
            for col in Churn.__table__.c
            if col.type.python_type.__name__ == col_type
        ]

    def column_values(self, column: str):
        with Session(self.engine) as s:
            result = s.query(getattr(Churn, column)).distinct().all()
            s.close()

            return result

    def user_counts(self):
        with Session(self.engine) as s:
            result = s.query(Churn.customerID).count()
            s.close()

            return result

    def categorical_distribution(self, column: str):
        with Session(self.engine) as s:
            result = (
                s.query(getattr(Churn, column), func.count(Churn.customerID))
                .group_by(getattr(Churn, column))
                .all()
            )
            s.close()
            return result

    def numerical_distribution(self, column: str):
        with Session(self.engine) as s:
            result = s.query(
                func.count(getattr(Churn, column)),
                func.round(func.sum(getattr(Churn, column))),
                func.round(func.avg(getattr(Churn, column))),
            ).first()
            s.close()
            return result
